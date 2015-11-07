class MultiAlignmentActionHandler:

    def __init__(self, alignments, reaction, action_handler):
        self.alignments = alignments
        self.reaction = reaction
        self.action_handler = action_handler

    def handle(self, action):
        all_thresholds_met = True
        for alignment in self.alignment:
            if not action.alignment.meets_threshold(alignment):
                all_thresholds_met = False
        if all_thresholds_met:
            return self.reaction
        else:
            return self.action_handler.handle(action)
