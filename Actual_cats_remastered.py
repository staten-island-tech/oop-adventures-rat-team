import pygame

class Cat:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)

        self.health = 50
        self.visible = False

        self.walk = 0
        self.walk_break = 0
        self.standing = True
        self.flip = False

        self.facing = "right"

        self.attack_cooldown = 5000
        self.last_attack_time = 0

        self.walks = ["walk1", "walk2", "walk3", "walk4", "walk5", "walk6"]

    def move_towards_player(self, player_pos):
        if self.pos.x < player_pos.x:
            self.pos.x += 2
            self.flip = False

        elif self.pos.x > player_pos.x:
            self.pos.x -= 2
            self.flip = True

        if self.pos.y < player_pos.y:
            self.pos.y += 2

        elif self.pos.y > player_pos.y:
            self.pos.y -= 2

    def get_rect(self):
        radius = 45
        surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)

        return surf.get_rect(center=(self.pos.x + 110, self.pos.y + 120))
    
    def attack(self, player_rect, current_time, rhealth):
        cat_rect = self.get_rect()

        attack_rect = pygame.Rect(0, 0, 90, 90)

        if self.facing == "right":
            attack_rect.midleft = (cat_rect.right + 10, cat_rect.centery)

        elif self.facing == "left":
            attack_rect.midright = (cat_rect.left - 10, cat_rect.centery)

        elif self.facing == "up":
            attack_rect.midbottom = (cat_rect.centerx, cat_rect.top - 10)

        elif self.facing == "down":
            attack_rect.midtop = (cat_rect.centerx, cat_rect.bottom + 10)

        if attack_rect.colliderect(player_rect):
            if current_time - self.last_attack_time >= self.attack_cooldown:
                rhealth[0] -= 10
                self.last_attack_time = current_time

        return attack_rect
    
    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.visible = False
            return True

        return False
    
    def draw(self, screen):
        image = pygame.image.load(f"cat_images\\{self.walks[self.walk]}.png")

        if self.flip:
            image = pygame.transform.flip(image, True, False)

        screen.blit(image, self.pos)