from .models import ConfigManager

# Singleton instance for easy access
config = ConfigManager.get
