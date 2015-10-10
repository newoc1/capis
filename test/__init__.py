from action.action import Action
from alignment.alignment import Alignment
from observer.observer import Observer
from subject.subject import Subject

alignment = Alignment(100, 100, 0, 0)
action = Action('destroy', alignment)

observer = Observer('observer', alignment, [action])
subject = Subject('subject', 'subject description')

subject.register_observer(observer)
subject.unregister_observer(observer)
subject.notify_observers()
