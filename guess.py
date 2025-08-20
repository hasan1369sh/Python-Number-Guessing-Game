import random

def select_game_level():
    """انتخاب سطح بازی با مدیریت خطا — تضمین می‌کنه خروجی عدد معتبر باشه"""
    while True:
        try:
            print('\n🎮 Choose your game level:')
            print('1️⃣  Easy: 10 guesses')
            print('2️⃣  Hard: 5 guesses')
            print('3️⃣  Beginner: Unlimited guesses')
            choice = int(input('Select (1, 2, or 3): '))
            if choice == 1:
                return 10
            elif choice == 2:
                return 5
            elif choice == 3:
                return float('inf')  # بی‌نهایت حدس
            else:
                print('❌ Please choose 1, 2, or 3.')
        except ValueError:
            print('❌ Invalid input! Please enter a number.')

def get_user_guess():
    """دریافت حدس کاربر با مدیریت خطا"""
    while True:
        try:
            return int(input('What do you think the number is? '))
        except ValueError:
            print('❌ Please enter a valid number.')

def generate_secret_number():
    """تولید عدد تصادفی بین 1 و 100"""
    return random.randint(1, 100)

def check_guess(secret, guess, attempt, max_guesses):
    """
    مقایسه حدس و بازگرداندن وضعیت بازی
    returns: (is_correct, remaining_guesses)
    """
    remaining = max_guesses - attempt if max_guesses != float('inf') else '∞'

    if guess < secret:
        print(f'\n📈 Too low! Remaining guesses: {remaining}\n')
    elif guess > secret:
        print(f'\n📉 Too high! Remaining guesses: {remaining}\n')
    else:
        print(f'\n🎉 Correct! You guessed it in {attempt} attempts!\n')
        return True, remaining
    return False, remaining

def play_game():
    """اجرای یک دور بازی"""
    print('\n🔢 A number between 1 and 100 has been selected. Let\'s start!\n')
    
    max_guesses = select_game_level()
    secret_number = generate_secret_number()
    attempt = 0

    while attempt < max_guesses:
        guess = get_user_guess()
        attempt += 1

        is_correct, remaining = check_guess(secret_number, guess, attempt, max_guesses)
        if is_correct:
            return True  # برد

        if max_guesses != float('inf'):
            if attempt >= max_guesses:
                print('💀 Game Over! You\'ve used all your guesses.')
                print(f'The correct number was: {secret_number}')
                return False  # باخت

    return False

def main():
    """مدیریت چرخه بازی (چندین دور)"""
    while True:
        play_game()
        print('-' * 50)
        play_again = input('🎮 Do you want to play again? (y/n): ').strip().lower()
        if play_again not in ['y', 'yes']:
            print('👋 Thanks for playing! Goodbye!')
            break

if __name__ == "__main__":
    main()
