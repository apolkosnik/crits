# CRITs Modernized Deployment Guide

This guide covers deployment options for the modernized CRITs framework running Django 4.2+ and Python 3.10+.

## Quick Start with Docker Compose (Recommended)

The fastest way to get CRITs running in production:

```bash
# Clone the repository
git clone <your-repo-url>
cd crits
git checkout updated

# Start CRITs with MongoDB
docker-compose up -d

# Wait for services to start, then create admin user
docker-compose exec crits python3 manage.py users -R UberAdmin \
  -u admin -p "YourSecurePassword123!" \
  -e "admin@yourorg.com" -f "Admin" -l "User" -o "Your Organization"

# Access CRITs at http://localhost:8080
```

## Docker Compose Architecture

The `docker-compose.yml` provides:
- **CRITs Application**: Django 4.2+ web application
- **MongoDB 6.0**: Document database with persistent storage
- **Networking**: Isolated container network
- **Volumes**: Persistent data and log storage

## Manual Docker Deployment

### Build and Run CRITs Container

```bash
# Build the image
docker build -t crits-modernized .

# Run with external MongoDB
docker run -d \
  --name crits-app \
  -p 8080:8080 \
  -e MONGO_HOST=your-mongodb-host \
  -e MONGO_DATABASE=crits \
  crits-modernized
```

### Run MongoDB Separately

```bash
# Start MongoDB container
docker run -d \
  --name crits-mongodb \
  -p 27017:27017 \
  -v mongodb_data:/data/db \
  mongo:6.0
```

## Traditional Installation

### Prerequisites
- Python 3.10 or higher
- MongoDB 6.0 or higher
- Git

### Installation Steps

```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt update
sudo apt install python3 python3-pip python3-dev build-essential
sudo apt install libldap2-dev libsasl2-dev libssl-dev libfuzzy-dev ssdeep libmagic1

# Clone and setup CRITs
git clone <your-repo-url>
cd crits
git checkout updated

# Install Python dependencies
pip3 install -r requirements.txt

# Start MongoDB (if not running)
sudo systemctl start mongod

# Run CRITs development server
python3 manage.py runserver 0.0.0.0:8080
```

## Production Configuration

### Environment Variables

```bash
# Required
export DJANGO_SETTINGS_MODULE=crits.settings
export MONGO_HOST=localhost
export MONGO_PORT=27017
export MONGO_DATABASE=crits

# Optional
export MONGO_USER=crits_user
export MONGO_PASSWORD=secure_password
export CRITS_DEBUG=False
```

### Security Hardening

1. **Update settings for production:**
   ```python
   # In crits/config/overrides.py
   DEBUG = False
   ALLOWED_HOSTS = ['your-domain.com', 'your-ip-address']
   SECURE_SSL_REDIRECT = True
   SECURE_COOKIE_SECURE = True
   ```

2. **Configure MongoDB authentication:**
   ```bash
   # Create MongoDB user
   mongo crits --eval "
   db.createUser({
     user: 'crits_user',
     pwd: 'secure_password',
     roles: ['readWrite']
   })"
   ```

3. **Set up reverse proxy (Nginx example):**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://localhost:8080;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## Initial Setup

### Create Admin User

```bash
python3 manage.py users -R UberAdmin \
  -u admin \
  -p "YourSecurePassword123!" \
  -e "admin@yourorg.com" \
  -f "Admin" \
  -l "User" \
  -o "Your Organization"
```

### Initialize Database

```bash
# Create default collections and indexes
python3 manage.py create_default_collections
python3 manage.py create_indexes
python3 manage.py create_roles
```

### Configure System Settings

```bash
# Set organization details
python3 manage.py setconfig company_name "Your Organization"
python3 manage.py setconfig instance_name "Production CRITs"
python3 manage.py setconfig instance_url "https://your-domain.com"
python3 manage.py setconfig classification "TLP:GREEN"
```

## Monitoring and Maintenance

### Health Checks

```bash
# Test installation
python3 manage.py test_install

# Run system checks
python3 manage.py check --deploy

# Test database connectivity
python3 manage.py shell -c "from mongoengine import connect; connect('crits')"
```

### Backup and Recovery

```bash
# Backup MongoDB
docker-compose exec mongodb mongodump --db crits --out /backup

# Restore from backup
docker-compose exec mongodb mongorestore --db crits /backup/crits
```

### Log Management

```bash
# View application logs
docker-compose logs crits

# View MongoDB logs
docker-compose logs mongodb

# Follow logs in real-time
docker-compose logs -f crits
```

## Troubleshooting

### Common Issues

1. **Port conflicts:**
   ```bash
   # Check what's using port 8080
   sudo netstat -tulpn | grep 8080
   
   # Use different port
   docker-compose up -d --scale crits=0
   docker-compose run -p 8081:8080 crits
   ```

2. **MongoDB connection issues:**
   ```bash
   # Check MongoDB status
   docker-compose exec mongodb mongo --eval "db.adminCommand('ping')"
   
   # Reset MongoDB data
   docker-compose down -v
   docker-compose up -d
   ```

3. **Permission issues:**
   ```bash
   # Fix Docker permissions
   sudo chown -R $USER:$USER .
   
   # Reset file permissions
   find . -type f -name "*.py" -exec chmod 644 {} \;
   ```

## Performance Optimization

### Production Recommendations

1. **Use Gunicorn for WSGI:**
   ```bash
   pip3 install gunicorn
   gunicorn --bind 0.0.0.0:8080 crits.wsgi:application
   ```

2. **Configure MongoDB for production:**
   ```yaml
   # Add to docker-compose.yml mongodb service
   command: mongod --wiredTigerCacheSizeGB 2
   ```

3. **Enable Django static file serving:**
   ```bash
   python3 manage.py collectstatic --noinput
   ```

## Scaling Considerations

### Multi-Instance Deployment

For high-availability deployments:

1. **Load balancer** (Nginx/HAProxy)
2. **Multiple CRITs instances**
3. **MongoDB replica set**
4. **Shared storage** for file uploads
5. **Redis** for session storage (optional)

### Container Orchestration

For Kubernetes deployment:
- Convert docker-compose.yml to Kubernetes manifests
- Use persistent volumes for MongoDB
- Configure ingress for external access
- Set up horizontal pod autoscaling

## Support and Updates

### Version Management

```bash
# Check current versions
python3 -c "import django; print('Django:', django.get_version())"
python3 -c "import mongoengine; print('MongoEngine:', mongoengine.__version__)"

# Update dependencies
pip3 install -r requirements.txt --upgrade
```

### Migration Path

This modernized version maintains compatibility with existing CRITs data:
- MongoDB collections remain unchanged
- User accounts and permissions preserved
- Analysis data and relationships maintained
- Service plugins may require updates for Python 3

For additional support, refer to:
- CRITs GitHub repository
- CRITs community documentation
- Django 4.2 documentation
- MongoEngine documentation