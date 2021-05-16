from DB import Dbhelper


def main():

    db=Dbhelper()

    while True:
        print('*******WELCOME TO DB WORLD*******')
        print()
        print('Press 1 to INSERT NEW USER.')
        print('Press 2 to DISPLAY SINGLE USER.')
        print('Press 3 to DISPLAY ALL USER.')
        print('Press 4 to DELETE A USER.')
        print('Press 5 to UPDATE A USER.')
        print('Press 6 to EXIT.')
        print()
        try:
            choice=int(input())
            if (choice==1):
                print('To insert a new user kindly give the details')
                ui=int(input('Unique user id in numbers: '))
                un=input('Enter the name of the user: ')
                up=input('Enter the phone number of user: ')
                db.insert_user(ui,un,up)
            elif (choice==2):
                uid=input('To display a user kindly give the userid: ')
                db.fetch_one(int(uid))
            elif (choice==3):
                print('Details in DB')
                print()
                db.fetch_all()
            elif (choice==4):
                uid=input('To Delete a user kindly give the userid: ')
                db.delete_user(int(uid))
            elif (choice==5):
                print('To update a user kindly give the details')
                ui=int(input('user id of user: '))
                un=input('Enter the new name of the user: ')
                up=input('Enter the new phone number of user: ')
                db.update_user(ui,un,up)
            elif (choice==6):
                break
            else:
                print('Invalid Input ! Try again.')
        except Exception as e:
            print(e)
            print('Invalid Details ! Try again. ')


#if module name of this file is __main__ only then program will run.
if __name__=='__main__':
    main()