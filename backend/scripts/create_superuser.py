from app.db.crud import create_user
from app.db.schemas import UserCreate
from app.db.session import SessionLocal

def input_credential() -> tuple:
    email: str = input("email:")
    password: str = input("password:")
    if email and password:
        if '@' not in email:
            print('Incorrect email!')
            input_credential()
        if len(password) < 8:
            print('password length must be atleast 8 character!')
            input_credential()

        return email, password
    print('Incorrect input. please try again!')
    input_credential()


def init(email: str, password: str) -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email=email,
            password=password,
            is_active=True,
            is_superuser=True,
        ),
    )


if __name__ == "__main__":
    promt = input("Create superuser?(y/n)")
    if promt == 'y':
        email, password = input_credential()
        init(email, password)
        print("Superuser created")
    else:
        print('Skipped superuser create')
