import enemy
import enemy_generator
# this is the main file for my protype pattern notes


def main():
    # create enemy
    enemy_prototype = enemy.Enemy(10, 5)
    big_enemy_prototype = enemy.BigEnemy(10, 5, 100)
    enemy_prototype.describe()
    big_enemy_prototype.describe()
    # create generator(?) for enemies with an enemy prototype
    small_generator = enemy_generator.EnemyGenerator(enemy_prototype)
    big_generator = enemy_generator.EnemyGenerator(big_enemy_prototype)
    test1 = small_generator.spawn()
    test1.describe()
    test2 = big_generator.spawn()
    test2.describe()
    # clone enemies
    # test with others

    pass


if __name__ == "__main__":
    main()
