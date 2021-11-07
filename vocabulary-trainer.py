import random
# import keyboard
import time

definitions_dict = {
  'Abate': 'Become less intense or widespread',
  'Abscond': 'Leave hurriedly and secretly, typically to avoid detection for something unlawful',
  'Acquiesce': 'Accept something reluctantly but without protest',
  'Acrimony': 'Biterness or ill feeling',
  'Acumen': 'The ability to make good judgments and quick decisions, typically in a particular domain',
  'Admonish': 'Reprimand firmly',
  'Adroit': 'Clever or skillful in using the hands or mind',
  'Adventitious': 'Happening or carried on according to chance rather than design or inherent nature',
  'Affectation': 'Behavior, speech, or writing that is artificial and designed to impress',
  'Alacrity': 'Brisk and cheerful readiness',
  'Ambivalent': 'Having mixed feelings or contradictory ideas about something or someone',
  'Ameliorate': 'Make (something bad or unsatisfactory) better',
  'Amicable': '(Of relations between people) Having a spirit of friendliness; without serious disagreement or rancor',
  'Apathy': 'Lack of interest, enthusiasm, or concern',
  'Aphasia': 'Loss of ability to understand or express speech, caused by brain damage',
  'Aphorism': 'A pithy observation that contains a general truth: "If it ain\'t broke, don\'t fix it"',
  'Apropos': 'With reference to; concerning',
  'Ardent': 'Very enthusastic or passionate',
  'Arduous': 'Involving or requiring strenuous effort; difficult and tiring',
  'Assent': 'The expression of approval or agreement',
  'Assiduous': 'Showing great care and perseverance',
  'Assuage': 'Make (an unpleasant feeling) less intense',
  'Austerity': 'Sternness or severity of manner or attitude',
  'Axiomatic': 'Self-evident or unquestionable',
  'Baleful': 'Threatening harm; menacing',
  'Beget': '(Typically of a man) Bring (a child) into existence by the process of reproduction',
  'Beguile': 'Charm or enchant, often in a deceptive way',
  'Beneficent': 'Generous or doing good',
  'Bereave': 'Be deprived of a loved one through a profound absence, especially due to death',
  'Bereft': 'Deprived of or lacking something, especially a nonmaterial asset',
  'Blithe': 'Showing a casual and cheerful indifference considered to be callous or improper',
  'Bloviate': 'Talk at length, especially in an inflated or empty way',
  'Bluster': 'Talk in a loud, aggressive, or indignant way with little effect',
  'Bombast': 'High-sounding language with little meaning, used to impress people',
  'Bonafide': 'Genuine; real',
  'Boon': 'A thing that is helpful or beneficial',
  'Bountiful': 'Large in quantity; abundant',
  'Brevity': 'Concise/exact use of words',
  'Brood': 'Think deeply about somehting that makes one unhappy',
  'Cacophony': 'A harsh, discordant mixture of sounds',
  'Calamitous': 'Catastrophic or disastrous',
  'Capricious': 'Given to sudden and unaccountable changes of mood or behaviour',
  'Candor': 'The quality of being open and honest in expression; frankness',
  'Cantankerous': 'Bad-tempered, argumentative, and uncooperative',
  'Castigate': 'Reprimand severely',
  'Cathartic': 'Providing psychological relief through the open expression of strong emotions',
  'Chagrin': 'Distress or embarrassment at having failed or been humiliated',
  'Chastise': 'Rebuke or reprimand severely',
  'Commensurate': 'Corresponding in size or degree; in proportion',
  'Comport': 'Conduct oneself; behave',
  'Compunction': 'A feeling of guilt or moral scruple that follows the doing of something bad',
  'Conflate': 'Combine (two or more text, ideas, etc.) into one',
  'Conciliatory': 'Intended or likely to placate or pacify',
  'Congenial': '(Of a person) Pleasant because of a personality, qualities, or interests that are similar to one\'s own',
  'Conjecture': 'An opinion or conclusion formed on the basis of incomplete information',
  'Consternation': 'Feelings of anxiety or dismay, typically at something unexpected',
  'Convalescent': '(Of a person) Recovering from an illness or operation',
  'Contemporaneous': 'Existing or occurring in the same period of time',
  'Contempt': 'Disapproval tinged with disgust',
  'Convivial': '(Of an atmosphere or event) Friendly, lively, and enjoyable / (Of a person) Cheerful and friendly; jovial',
  'Copacetic': 'In excellent order',
  'Coven': 'A group or gathering of witches who meet regularly',
  'Credence': 'Belief in or acceptance of something as true',
  'Credulous': 'Having or showing too great a readiness to believe things',
  'Curmudgeon': 'A bad-tempered person, especially an old one',
  'Cursory': 'Hasty and therefore not thorough or detailed',
  'Dearth': 'A scarcity or lack of something',
  'Debase': 'Reduce (something) in quality or value; degrade',
  'Debonair': '(Of a man) Confident, stylish, and charming',
  'Deference': 'Humble submission and respect',
  'Deign': 'Do something that one considers to be beneath one\'s dignity',
  'Deleterious': 'Causing harm or damage',
  'Deluge': 'A great quantity of something arriving at the same time; a severe flood',
  'Denigrate': 'Criticize unfairly; disparage',
  'Derelict': 'In very poor condition as a result of disuse and neglect',
  'Derisive': 'Expressing contempt or ridicule',
  'Destitute': 'Without the basic necessities of life',
  'Diatribe': 'A forceful and bitter verbal attack',
  'Dichotomy': 'A division or contrast between two things that are or are represented as being opposed or entirely different',
  'Diminutive': 'Extremely or unusually small',
  'Discordant': 'Disagreeing or incongruous',
  'Discourse': 'Written or spoken communication or debate',
  'Discursive': 'Digressive from subject to subject',
  'Disdain': 'The feeling that someone/something is unworthy of one\'s consideration or respect',
  'Disquieting': 'Inducing feelings of anxiety or worry',
  'Dissention': 'Disagreement that leads to discord',
  'Docile': 'Ready to accept control or instruction; submissive',
  'Dreck': 'Rubbish; trash',
  'Dubious': 'Hesitating or doubting',
  'Eclectic': 'Deriving ideas, style, or taste from a broad and diverse range of sources',
  'Edification': 'The instruction or improvement of a person morally or intellectually',
  'Edifice': 'A building, especially a large, imposing one',
  'Efface': 'Erase (a mark) from a surface',
  'Effusive': 'Expressing feelings or gratitude, pleasure, or approval in an unrestrained or heartfelt manner',
  'Eloquent': 'Fluent or persuasive in speaking or writing',
  'Elucidate': 'Make (something) clear; explain',
  'Emancipate': 'Set free from restrictions',
  'Encroach': 'Intrude on',
  'Enigma': 'A person or thing that is mysterious or difficult to understand',
  'Enkindle': 'Arouse or inspire (an emotion); set on fire',
  'Enmity': 'The state or feeling of being actively opposed or hostile to someone or something',
  'Ephemeral': 'Lasting for a very short time',
  'Epistemological': 'The theory of knowledge, especially with regard to its methods, validity, and scope',
  'Equanimity': 'Mental calmness, composure, and evenness of temper, especially in a difficult situation',
  'Ersatz': 'Made or used as a substitute, typically an inferior one, for something else',
  'Erudite': 'Having or showing great knowledge or learning',
  'Erudition': 'The quality of having or showing great knowledge or learning; scholarship',
  'Esoteric': 'Intended for or likely to be understood by only a small number of people with a specialized knowledge or interest',
  'Etymology': 'The study of the origin of words and the way in which their meanings have changed throughout history',
  'Euphemism': 'Mild word/expression substituted for one considered too harsh when referring to something unpleasant',
  'Evanescent': 'Soon passing out of sight, memory, or existence',
  'Excoriate': 'Censure or criticize severely',
  'Exculpate': 'Show or declare that (someone) is not guilty of wrongdoing',
  'Exhort': 'Strongly encourage or urge (someone) to do something',
  'Exiguous': 'Very small in size or amount',
  'Expedient': '(Of an action) Convenient and practical, although possibly improper or immoral',
  'Expound': 'Present and explain (a theory or idea) systematically and in detail',
  'Extant': 'Still in existence; surviving',
  'Extemporaneous': 'Spoken or done without preparation',
  'Exude': '(Of a person) Display (an emotion or quality) strongly and openly',
  'Facetious': 'Treating serious issues with deliberately inappropriate humor; flippant',
  'Facsimile': 'An exact copy, especially of written or printed material',
  'Faff': 'Spend time in ineffectual activity',
  'Fastidious': 'Very attentive to and concerned about accuracy and detail',
  'Febrile': 'Having or showing the symptoms of a fever',
  'Feign': 'Pretend to be affected by (a feeling, state)',
  'Felicitous': 'Well chosen or suited to the circumstances',
  'Fervor': 'Intense and passionate feeling',
  'Fetid': 'Smelling extremely unpleasant',
  'Fleeting': 'Lasting for a very short time',
  'Flippant': 'Not showing a serious or respectful attitude',
  'Furtive': 'Attempting to avoid notice or attention, typically because of guilt or a belief that discovery would lead to trouble; secretive',
  'Gaffe': 'An unintentional act causing embarrassment',
  'Gallant': '(Of a person or their behavior) Brave; heroic',
  'Galling': 'Annoying; angering; humiliating',
  'Galvanize': 'Shock or excite (someone), typically into taking action',
  'Gamut': 'The complete range or scope of something',
  'Garish': 'Obtrusively bright and showy',
  'Gaudy': 'Extravagantly bright or showy, typically so as to be tasteless',
  'Glean': 'Extract (information) from various sources',
  'Glib': 'Fluent, but insincere or shallow',
  'Glower': 'Have an angry or sullen look on one\'s face; scowl',
  'Goad': 'Provoke or annoy (someone) so as to stimulate some action or reaction',
  'Gossamer': 'Used to refer to something very light, thin, and insubstantial or delicate',
  'Gratuitous': 'Uncalled for; lacking good reason, unwarranted',
  'Gregarious': '(Of a person) Fond of company; sociable',
  'Hedonistic': 'Overly theatrical or melodramatic in character or style',
  'Hubris': 'Excessive pride or self-confidence',
  'Immiserate': 'To make miserable',
  'Immutable': 'Unchanging over time or unable to be changed',
  'Impasse': 'A situation in which no progress is possible, especially because of disagreement',
  'Impetuous': 'Acting or done quickly and without thought or care',
  'Impetus': 'The force or energy with which a body moves',
  'Impoverish': 'Make (a person or area) poor',
  'Impugn': 'Dispute the truth, validity, or honesty of (a statement of motive); call into question',
  'Impunity': 'Exemption from punishment or freedom from the injurious consequences of an action',
  'Inadvertent': 'Not resulting from or achieved through deliberate planning',
  'Incessantly': 'Without interruption; constant',
  'Incongruous': 'Not in harmony or keeping with the surroundings or other aspects of something',
  'Incorrigible': '(Of a person or their tendencies) Not able to be corrected, improved, or reformed',
  'Indifference': 'Lack of interest, concern, or sympathy',
  'Indignant': 'Feeling or showing anger or annoyance at what is perceived as unfair treatment',
  'Ineluctable': 'Unable to be resisted or avoided; inescapable',
  'Inexorable': 'Impossible to stop or prevent',
  'Inimical': 'Tending to obstruct or harm',
  'Injurious': 'Causing or likely to cause damage or harm',
  'Innate': 'Inborn; natural',
  'Innocuous': 'Not harmful or offensive',
  'Inoculate': 'Treat (a person or animal) with a vaccine to produce immunity against a disease',
  'Inscrutable': 'Impossible to understand or interpret',
  'Insidious': 'Working or spreading in a hidden and usually injurious way',
  'Insipid': 'Lacking flavor',
  'Interlocutor': 'A person who takes part in a conversation or dialogue',
  'Interminable': 'Endless (often used hyperbolically)',
  'Inundate': 'Overwhelm (someone) with things or people to be dealt with',
  'Invidious': 'Likely to arouse or incur resentment or anger in others',
  'Inviolable': 'Never to be broken, infringed, or dishonored',
  'Ipsilaterable': 'Belonging to or occurring on the same side of the body',
  'Lackadaisical': 'Lacking enthusiasm and determination; carelessly lazy',
  'Laconic': '(Of a pesron, style of writing) Using very few words',
  'Laudable': 'Deserving praise and commendation',
  'Leery': 'Cautious or wary due to realistic suspicions',
  'Lethargy': 'A lack of energy and enthusiasm',
  'Levity': 'Treatment of a serious matter with humor or lack of due respect',
  'Malign': 'Evil in nature or effect; malevolent',
  'Mete': 'Dispense or allot justice, a punishment, or harsh treatment',
  'Minutiae': 'The small, precise, or trivial details of something',
  'Misanthrope': 'A person who dislikes humankind and avoids human society',
  'Modicum': 'A small quantity of a particular thing, especially something considered desirable or valuable',
  'Multifarious': 'Many and of various types',
  'Nefarious': '(Typically of an action or activity) Wicked or criminal',
  'Nicety': 'A fine detail or distinction, especially one regarded as intricate and fussy',
  'Niggle': 'Cause slight but persistent annoyance, discomfort, or anxiety',
  'Nonchalant': '(Of a person or manner) Feeling or appearing casually calm and relaxed; not displaying anxiety, interest, or enthusiasm',
  'Non sequitur': 'A conclusion or statement that does not logically follow from the previous argument or statement',
  'Numinous': 'Having a strong religious or spiritual quality; indicating or suggesting the presence of a divinity',
  'Obeisance': 'Deferential respect',
  'Obfuscate': 'Render obscure, unclear, or unintelligible',
  'Obstinate': 'Stubbornly refusing to change one\'s opinion or chosen course of action, despite attempts to persuade one to do so',
  'Omniscient': 'Knowing everything',
  'Onerous': '(Of a task) Involving an amount of effort and difficulty that is oppressively burdensome',
  'Ontology': 'The philosophical study of the nature of being, becoming, existence',
  'Onus': 'Something that is one\'s duty or responsibility',
  'Opulent': 'Ostentatiously costly and luxurious',
  'Ostensibly': 'Apparently or purportedly, but perhaps not actually',
  'Ostentatious': 'Characterized by vulgar or pretentious display; designed to impress or attract notice',
  'Palpable': 'Able to be touched or felt',
  'Paragon': 'A person or thing regarded as a perfect example of a particular quality',
  'Parsimonious': 'Unwilling to spend money or use resources; stingy or frugal',
  'Pejorative': 'Expressing contempt or disapproval',
  'Pensive': 'Engaged in deep or serious thought',
  'Perfunctory': 'Carried out with a minimum of effort or reflection',
  'Pernicious': 'Having a harmful effect, especially in a gradual or subtle way',
  'Perennial': 'Lasting or existing for a long or apparently infinite time; enduring',
  'Pervade': 'Spread through and be perceived in every part of',
  'Petulant': 'Childishly sulky or bad-tempered',
  'Piety': 'The quality of being religious or reverent',
  'Pious': 'Devoutly religious',
  'Pithy': '(Of language or style) Concise and forcefully expressive',
  'Platitude': 'A remark or statement, especially one with a moral content, that has been used too often to be interesting or thoughtful',
  'Poignant': 'Evoking a keen sense of sadness or regret',
  'Polymath': 'A person of wide-ranging knowledge or learning',
  'Pontificate': 'Express one\'s opinions in a way considered annoyingly pompous and dogmatic',
  'Posit': 'Assume as a fact; put forward as a basis of argument',
  'Precarious': 'Dependent on chance; uncertain',
  'Precept': 'A general rule intended to regulate behavior',
  'Precipitate': 'Cause (an event or situation, typically one that is undesirable) to happen suddenly',
  'Prescient': 'Having or showing knowledge of events before they take place',
  'Pretense': 'An attempt to make something that is not the case appear true',
  'Primacy': 'The fact of being primary, preeminent, or more important',
  'Proclivity': 'An inclination or predisposition toward a particular thing',
  'Propitiate': 'Win or regain the favor of someone by doing something pleasing',
  'Proprioception': 'The unconscious perception of movement and spatial orientation arising from stimuli within the body itself',
  'Prototypical': 'Denoting the first, original, or typical form of something',
  'Proverbial': 'Well known, especially so as to be stereotypical',
  'Provocation': 'Action or speech that makes someone annoyed or angry, especially deliberate',
  'Punitive': 'Inflicting or intended as punishment',
  'Purview': 'The scope of the influence or concerns of something',
  'Putative': 'Generally regarded or reputed to be',
  'Quandary': 'A state of perplexity or uncertainty over what to do in a difficult situation',
  'Querulous': 'Complaining in a petulant or whining manner',
  'Quiescent': 'In a state or period of inactivity or dormancy',
  'Quintessence': 'The most perfect or typical example of a quality or class',
  'Quixotic': 'Exceedingly idealistic; unrealistic and impractical',
  'Rancor': 'Bitterness or resentfulness, especially when long-standing',
  'Rebuff': 'Reject (someone or something) in an abrupt or ungracious manner',
  'Rebuke': 'Express sharp disapproval of someone because of their behavior/actions',
  'Recapitulate': 'Summarize and state again the main points of',
  'Reconcile': 'Restore friendly relations between',
  'Redolent': 'Strongly remeniscent or suggestive of',
  'Reify': 'Make (something abstract) more concrete or real',
  'Rejoinder': 'A reply, especially a sharp or witty one',
  'Replete': 'Filled or well-supplied with something',
  'Reprehensible': 'Deserving censure or condemnation',
  'Reproach': 'Express disappointment in one\'s actions',
  'Repudiate': 'Refuse to accept or be associated with',
  'Repugnant': 'Extremely distasteful; unacceptable',
  'Reticent': 'Not revealing one\'s thoughts or feelings readily',
  'Reverie': 'A state of being pleasantly lost in one\'s thoughts; a daydream',
  'Revile': 'Criticize in an angry, insulting manner',
  'Rigmarole': 'A lengthy and complicated procedure',
  'Rigor': 'The quality of being extremely thorough, exhaustive, or accurate',
  'Rive': 'Split or tear apart violently',
  'Robust': 'Strong and healthy; vigorous',
  'Roil': 'To cause (someone or something) to become very agitated or disturbed',
  'Rue': 'Bitterly regret',
  'Ruminate': 'Think deeply about something',
  'Salient': 'Most noticeable or important',
  'Sanctimonious': 'Making a show of being morally superior to other people',
  'Sanguine': 'Optimistic or positive, especially in a bad situation',
  'Sardonic': 'Grimly mocking or cynical',
  'Sartorial': 'Of or relating to tailoring, clothes, or style of dress',
  'Schadenfreude': 'Pleasure derived by someone from another person\'s misfortune',
  'Scintilla': 'A tiny trace or spark of a specified quality or feeling',
  'Scrupulous': 'Diligent, thorough, and extremely attentive to details',
  'Shorn': 'Past participate of \'shear\'',
  'Sillage': 'How a fragrance lingers in the air',
  'Snide': 'Derogatory or mocking in an indirect way',
  'Snit': 'A fit of irritation; a sulk',
  'Soporific': 'Tending to induce drowsiness or sleep',
  'Spurious': 'Not being what it purports to be; false',
  'Stark': 'Severe or bare in appearance or outline',
  'Stifle': 'Restrain (a reaction) or stop oneself acting on (an emotion)',
  'Stoic': 'A person who can endure pain or hardship without showing their feelings or complaining',
  'Strident': 'Loud and harsh; grating',
  'Suave': '(Especially of a man) Charming, confident, and elegant',
  'Surly': 'Bad-tempered and unfriendly',
  'Surmise': 'Suppose that something is true without having evidence to confirm it',
  'Surreptitious': 'Kept secret, especially because it would not be approved of',
  'Tacit': 'Understood or implied without being stated',
  'Tantamount': 'Equivalent in seriousness to; virtaully the same as',
  'Tawdry': 'Showy but cheap and of poor quality',
  'Temerity': 'Excessive confidence or boldness; audacity',
  'Tenacity': 'Persistent; being very determined',
  'Tenuous': 'Very weak or slight',
  'Tepid': 'Only slightly warm; lukewarm',
  'Terse': 'Sparing in the use of words; abrupt',
  'Trepidation': 'A feeling of fear or agitation about something that may happen',
  'Trite': '(Of a remark, opinion, or idea) Overused and consequently of little import; lacking originality or freshness',
  'Truism': 'A statement that is obviously true and says nothing new or interesting',
  'Umbrage': 'Offense or annoyance',
  'Vacillate': 'Waver between different opinions or actions; be indecisive',
  'Vapid': 'Offering nothing that is stimulating or challenging',
  'Vaunt': 'Boast about or praise',
  'Vehement': 'Showing strong feeling; forceful, passionate, or intense',
  'Venerate': 'Regard with great respect; revere',
  'Veracity': 'Conformity to facts; accuracy',
  'Veridical': 'Truthful',
  'Verisimilitude': 'The appearance of being true or real',
  'Vicarious': 'Experienced in the imagination through the feelings or actions of another person',
  'Vigor': 'Strength, energy, or determination',
  'Vilify': 'Speak or write about in an abusively disparaging manner',
  'Vindicate': 'Clear (someone) of blame or suspicion',
  'Virile': '(Of a man) Having strength, energy, and a strong sex drive',
  'Visceral': 'Relating to deep inward feelings rather than to the intellect',
  'Vitiate': 'Spoil or impair the quality or efficiency of',
  'Vitriol': 'Cruel and bitter criticism',
  'Vociferous': '(Especially of a person or speech) Vehement or clamorous',
  'Wont': '(Of a person) In the habit of doing something; accustomed',
  'Wraith': 'A ghost or ghostlike image of someone, especially seen shortly before or after their death',
  'Xenophobia': 'Intense or irrational dislike or fear of people from other countries',
}


class Word:

    score = 0
    words_used = []

    def __init__(self, word, definition, number, number_of_words):
        self.word = word
        self.definition = definition
        self.length = len(word)
        self.letters_shown = 0
        self.number = number
        self.number_of_words = number_of_words
        self.cannot_score = False

        print('\n\n' + '-'*len(self.definition) + '\n' + self.definition + '\n' + '-'*len(self.definition))
        self.run()

    def run(self, print_score=True):

        Word.words_used.append(self.word)
        guess = input('Word: ').strip().lower()
        if guess == self.word.strip().lower() and self.cannot_score is False:
            Word.score += 1

            print('\n***********\n* CORRECT *\n***********')

        elif guess == '=':
            self.cannot_score = True
            done = self.show_letter_hint()
            if done is True:
                return
            else:
                self.run(print_score=False)

            if print_score is True:
                print(self.word)

        elif print_score is True:
            print('\nINCORRECT')
            print('The answer was: ' + self.word)

        if self.number == self.number_of_words - 1 and print_score is True:
            print('\nFINAL SCORE: {}/{}: {}%\n'.format(Word.score, self.number + 1, str(round((Word.score/(self.number + 1)) * 100, 1))))
            print(', '.join(set(Word.words_used)) + '\n')
        elif print_score is True:
            print('\nCurrent Score: {}/{}'.format(Word.score, self.number + 1))

    def show_letter_hint(self):
        if self.letters_shown < self.length:
            self.letters_shown += 1
            print(self.word[0:self.letters_shown])

        if self.letters_shown == self.length:
            return True
            

def get_number_of_words():
    print('')
    number_of_words = input('Number of words to train on: ').strip()
    try:
        number_of_words = int(number_of_words)
        if number_of_words <= 0 or number_of_words > len(definitions_dict):
            1/0
        return number_of_words
    except Exception:
        get_number_of_words()


number_of_words = get_number_of_words()
indexes_used = []

def generate_index():
    return random.randint(0, len(definitions_dict)-1)

def process_index():
    index = generate_index()
    while index in indexes_used:
        index = generate_index()
    indexes_used.append(index)
    return index

for number in range(number_of_words):
    index = process_index()
    word_to_use, definition_to_use = list(definitions_dict.items())[index]
    word_object = Word(word_to_use, definition_to_use, number, number_of_words)
