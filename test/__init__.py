from alignment.alignment import Alignment
from observer.observer import Observer
from subject.subject import Subject
from subject.public_action import PublicAction
from subject.environment_items.apple import Apple


def apple_handler(observer, action):
    observed_apple = observer.subject.environment_item
    if observed_apple.state == observed_apple.AppleState.eaten and action.invoker == observer:
        print('%s said: "That was a tasty apple"' % observer.name)
    elif observed_apple.state == observed_apple.AppleState.eaten and action.invoker != observer:
        print('%s "I will take revenge on the apple eater"' % observer.name)
    else:
        print('%s I want to eat that apple' % observer.name)


chaoticEvil = Alignment(100, 100, 0, 0)
chaoticEvilObserver = Observer('chaevil', chaoticEvil, apple_handler)

lawfulGood = Alignment(0, 0, 100, 100)
lawfulGoodObserver = Observer('lawgood', lawfulGood, apple_handler)

apple = Apple()
subject = Subject(apple)

subject.register_observer(chaoticEvilObserver)
subject.register_observer(lawfulGoodObserver)

eatAppleCommand = PublicAction('eat_apple', chaoticEvil, chaoticEvilObserver, 'eat')

chaoticEvilObserver.update_subject(eatAppleCommand)
