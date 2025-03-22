import os

def get_asset_path(*path_parts):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(BASE_DIR, *path_parts)

# # Ví dụ dùng hàm:
# image = pygame.image.load(get_asset_path("images", "piece.png"))
# icon = pygame.image.load(get_asset_path("icons", "game.ico"))
