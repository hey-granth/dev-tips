import json
from pathlib import Path
from typing import Dict, List, Any

class ConfigManager:
    def __init__(self, config_dir: Path = None):
        if config_dir is None:
            config_dir = Path.home() / '.devtips'
        self.config_dir = config_dir
        self.config_path = self.config_dir / 'config.json'
        self.tips_path = self.config_dir / 'tips.json'

        self._ensure_config_dir()
        self.config = self._load_config()
        self.tips = self._load_tips()

    # creating the config directory if it doesn't exist
    def _ensure_config_dir(self):
        self.config_dir.mkdir(parents=True,exist_ok=True)

    # loading the config from the config file
    def _load_config(self) -> Dict[str, Any]:
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                return json.load(f)

        default_config = {
            'notification_time': '09:00',
            'topics': ['python', 'javascript', 'devops', 'git'],
            'enabled': True
        }
        self.save_config(default_config)
        return default_config

    # loading the tips from the tips file
    def _load_tips(self) -> Dict[str, List[str]]:
        if self.tips_path.exists():
            with open(self.tips_path, 'r') as f:
                return json.load(f)

        # tips to be updated later on
        default_tips = {
            'python': ['Tip 1', 'Tip 2'],
            'javascript': ['Tip 3', 'Tip 4'],
            'devops': ['Tip 5', 'Tip 6'],
            'git': ['Tip 7', 'Tip 8']
        }
        self.save_tips(default_tips)
        return default_tips

    # saving the config to the config file
    def save_config(self, config: Dict[str, Any] = None):
        config = config or self.config
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=4)
        self.config = config

    # saving the tips to the tips file
    def save_tips(self, tips: Dict[str, List[str]] = None):
        tips = tips or self.tips
        with open(self.tips_path, 'w') as f:
            json.dump(tips, f, indent=4)
        self.tips = tips

    # updating the config
    def update_config(self, **kwargs):
        self.config.update(kwargs)
        self.save_config()
