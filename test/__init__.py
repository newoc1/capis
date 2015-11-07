from alignment.alignment import Alignment
from observer.observer import Observer
from subject.subject import Subject
from persona.action.public_action import PublicAction
from subject.environment_items.apple import Apple
from subject.environment_items.person import Person
from persona.persona import Persona
from test.action_handlers_factory import create_chaotic_evil_handlers, create_lawful_good_handlers

#initialize alignments
chaoticEvil = Alignment(90, 75, 0, 0)
lawfulGood = Alignment(0, 0, 80, 80)

#initialize chaotic evil persona
chaevil_health = 100
chaevil_action_handlers = create_chaotic_evil_handlers()
chaevil_person = Person(chaevil_health)
chaevil_subject = Subject('person', chaevil_person)
chaevil_person_observer = Observer()
chaevil_subject.register_observer(chaevil_person_observer)
chaevil = Persona('chaevil', chaoticEvil, chaevil_subject, chaevil_action_handlers)
chaevil.add_observer(chaevil_person_observer)

#initialize lawful good persona
lawgood_health = 100
lawgood_action_handlers = create_lawful_good_handlers()
lawgood_person = Person(lawgood_health)
lawgood_subject = Subject('person', lawgood_person)
lawgood_person_observer = Observer()
lawgood_subject.register_observer(lawgood_person_observer)
lawgood = Persona('lawgood', lawfulGood, lawgood_subject, lawgood_action_handlers)
lawgood.add_observer(lawgood_person_observer)

#apple observer for chaevil
chaevil_apple_observer = Observer()
chaevil.add_observer(chaevil_apple_observer)
#apple observer for lawgood
lawgood_apple_observer = Observer()
lawgood.add_observer(lawgood_apple_observer)

#initialize apple and subject. Register observers of apple
apple = Apple()
apple_subject = Subject('apple',apple)
apple_subject.register_observer(lawgood_apple_observer)
apple_subject.register_observer(chaevil_apple_observer)

#define eat apple action for chaevil to execute
eat_apple_action = PublicAction('eat_apple', chaoticEvil, 'eat')

chaevil.execute(eat_apple_action,apple_subject)
