from handlers.attend_handler import attend_loop

if __name__ == "__main__":
    portal = input("Выберите портал (pge — магистратура, wsp — бакалавриат): ").strip().lower()
    if portal not in ["pge", "wsp"]:
        print("Некорректный выбор! Использую pge по умолчанию.")
        portal = "pge"
    attend_loop(portal)