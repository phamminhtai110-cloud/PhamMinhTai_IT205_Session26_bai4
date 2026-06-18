from abc import ABC, abstractmethod


class Equipment(ABC):
    @abstractmethod
    def calculate_total_damage(self):
        pass


class Weapon(Equipment):
    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name.title()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp/so sánh giữa các trang bị!")
            return False

        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp/so sánh giữa các trang bị!")
            return None

        return Weapon(
            f"Fusion({self.name} + {other.name})",
            self.base_damage + other.base_damage,
            self.upgrade_level + other.upgrade_level
        )


class MagicMixin:
    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print(f"{self.name} phát sáng ma thuật!")


class MagicSword(Weapon, MagicMixin):
    def __init__(self, name, base_damage, upgrade_level, magic_power):
        Weapon.__init__(self, name, base_damage, upgrade_level)
        MagicMixin.__init__(self, magic_power)

    def calculate_total_damage(self):
        return (
            self.base_damage
            + self.upgrade_level * 10
            + self.magic_power
        )


inventory = []


def input_positive(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Giá trị phải lớn hơn 0!")
                continue
            return value
        except ValueError:
            print("Dữ liệu không hợp lệ!")


while True:
    print("\n===== LÒ RÈN VŨ KHÍ =====")
    print("1. Xem kho")
    print("2. Rèn Weapon")
    print("3. Rèn MagicSword")
    print("4. Thẩm định")
    print("5. Dung hợp")
    print("6. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        if not inventory:
            print("Kho vũ khí hiện đang trống.")
            continue

        for i, item in enumerate(inventory, 1):
            print(
                f"{i}. {item.name} | "
                f"{type(item).__name__} | "
                f"Level {item.upgrade_level} | "
                f"Damage {item.calculate_total_damage()}"
            )

    elif choice == "2":
        name = input("Tên vũ khí: ")
        damage = input_positive("Sát thương gốc: ")
        level = input_positive("Cấp cường hóa: ")

        inventory.append(
            Weapon(name, damage, level)
        )

        print("Rèn Weapon thành công!")

    elif choice == "3":
        name = input("Tên kiếm: ")
        damage = input_positive("Sát thương gốc: ")
        level = input_positive("Cấp cường hóa: ")
        magic = input_positive("Sức mạnh phép thuật: ")

        inventory.append(
            MagicSword(name, damage, level, magic)
        )

        print("Rèn MagicSword thành công!")

    elif choice == "4":
        if len(inventory) < 2:
            print("Cần ít nhất 2 vũ khí!")
            continue

        w1 = inventory[0]
        w2 = inventory[1]

        if w1 > w2:
            print(f"{w1.name} mạnh hơn {w2.name}")
        elif w2 > w1:
            print(f"{w2.name} mạnh hơn {w1.name}")
        else:
            print("Hai vũ khí ngang sức nhau")

    elif choice == "5":
        if len(inventory) < 2:
            print("Cần ít nhất 2 vũ khí!")
            continue

        new_weapon = inventory[0] + inventory[1]

        if new_weapon:
            inventory.pop(0)
            inventory.pop(0)
            inventory.append(new_weapon)

            print("Dung hợp thành công!")
            print(new_weapon.name)

    elif choice == "6":
        print("Thoát Lò Rèn. Hẹn gặp lại Anh hùng!")
        break

    else:
        print("Lựa chọn không hợp lệ!")