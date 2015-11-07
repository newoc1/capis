from alignment.alignment import Alignment
from persona.action.public_action import PublicAction
from persona.action_handlers.alignment_action_handler import AlignmentActionHandler
from persona.action_handlers.terminal_action_handler import TerminalActionHandler
from persona.reaction.invoker_reaction import InvokerReaction

chaotic_evil_align = Alignment(50,50,0,0)
lawful_good_align = Alignment(0, 0, 100, 100)

def create_lawful_good_handlers():
    lawful_good_handlers = []
    damage_amount= 10

    chaotic_evil_hit = PublicAction('chaotic_evil_hit', lawful_good_align, 'damage', damage_amount)
    reaction_to_chaotic_evil = InvokerReaction(chaotic_evil_hit, 'person')
    lawful_good_handlers.append(AlignmentActionHandler(chaotic_evil_align, reaction_to_chaotic_evil, TerminalActionHandler()))
    return lawful_good_handlers

def create_chaotic_evil_handlers():
    chaotic_evil_handlers = []
    damage_amount= 10
    lawful_good_hit = PublicAction('lawful_good_hit', chaotic_evil_align, 'damage', damage_amount)
    reaction_to_lawful_good = InvokerReaction(lawful_good_hit, 'person')
    chaotic_evil_handlers.append(AlignmentActionHandler(lawful_good_align, reaction_to_lawful_good, TerminalActionHandler()))
    return chaotic_evil_handlers