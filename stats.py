

#Job list (to be used by party)
JOB_LIST = []

#Euip list (to be used by party)
EQUIP_LIST = []

#Convert aptitudes characters to their stats multipliers
def convert_aptitude(rank):

	if rank == "S":
		return 1.35
	if rank == "A":
		return 1.19
	if rank == "B":
		return 1
	if rank == "C":
		return 0.9
	if rank == "D":
		return 0.8
	if ranl == "E":
		return 0.7


class stats():

	#DEFINING BASE STATS (LEVEL 1, B RANK)
	def __init__(self, hp, mp, weight, patk, pdef, matk, mdef, mnd, spe, aim, eva, luck, tgt):
		self.HP = hp
		self.MP = mp
		self.WEIGHT = weight
		self.PATK = patk
		self.PDEF = pdef
		self.MATK = matk
		self.MDEF = mdef
		self.MND = mnd
		self.SPE = spe
		self.AIM = aim
		self.EVA =eva
		self.LUCK = luck
		self.TGT = tgt

		# BASE_STATS saves all rank B stats to changes aptitudes multiplying
		self.BASE_STATS = [hp, mp, weight, patk, pdef, matk, mdef, mnd, spe, aim, eva, luck, tgt]
		self.APT = ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"]

	def modify_stat_aptitudes():

		#Modify stats based in aptitudes
		self.HP = self.BASE_STATS[0] * convert_aptitude(self.APT[0])
		self.MP = self.BASE_STATS[1] * convert_aptitude(self.APT[1])
		self.WEIGHT = self.BASE_STATS[2] * convert_aptitude(self.APT[2])
		self.PATK = self.BASE_STATS[3] * convert_aptitude(self.APT[3])
		self.PDEF = self.BASE_STATS[4] * convert_aptitude(self.APT[4])
		self.MATK = self.BASE_STATS[5] * convert_aptitude(self.APT[5])
		self.MDEF = self.BASE_STATS[6] * convert_aptitude(self.APT[6])
		self.MND = self.BASE_STATS[7] * convert_aptitude(self.APT[7])
		self.SPE = self.BASE_STATS[8] * convert_aptitude(self.APT[8])
		self.AIM = self.BASE_STATS[9] * convert_aptitude(self.APT[9])
		self.EVA = self.BASE_STATS[10] * convert_aptitude(self.APT[10])
		self.LUCK = self.BASE_STATS[11] * convert_aptitude(self.APT[11])
		self.TGT = self.BASE_STATS[12] * convert_aptitude(self.APT[12])


	#Used to change aptitudes (when change job for example), self.APT will change their data and then stats will change
	def modify_aptitudes(apt):


		for i in range(len(apt)):
			self.APT = apt[i]
		self.modify_stat_aptitudes()


	#Used to modify BASE_STATS when level up, the other stats change too
	def modify_by_level(lvl,apt):

		self.BASE_STATS[0] = round(203 + (73*lvl))		#HP
		self.BASE_STATS[1] = round(184 + (6*lvl))		#MP 
		self.BASE_STATS[2] = round(10 + (1.158*lvl))	#WEIGHT
		self.BASE_STATS[3] = round(17 + (1.92*lvl)) 	#PATK
		self.BASE_STATS[4] = round(17 + (1.92*lvl))		#PDEF
		self.BASE_STATS[5] = round(17 + (1.92*lvl))		#MATK
		self.BASE_STATS[6] = round(17 + (1.92*lvl))		#MDEF
		self.BASE_STATS[7] = round(17 + (1.92*lvl))		#MND
		self.BASE_STATS[8] = round(17 + (1.92*lvl))		#SPE
		self.BASE_STATS[9] = round(91 + (2.333*lvl))	#AIM
		self.BASE_STATS[10] = round(17 + (1.92*lvl))	#EVA
		self.BASE_STATS[11] = round(1 + (0.14*lvl))		#LUCK
		self.BASE_STATS[3] = round(1 + (0.14*lvl))		#TGT

		self.modify_stat_aptitudes(apt)





class elemental_resistance():

	#SETTING ELEMENTAL RESISTANSE (-1, 0, +1, +2, +3)
	#CHARACTERS MUST HAVE 0 IN EVERYTHING BY DEFAULT

	def __init__(self, fire, ice, lightning, water, wind, earth, light, dark):

		self.FIRE = fire
		self.ICE = ice
		self.LIGHTNING = lightning
		self.WATER = water
		self.WIND = wind
		self.EARTH = earth
		self.LIGHT = light
		self.DARKNESS = dark



class level():

	def __init__(self, lvl = 1, exp = 0, formula = 2.718*2.718*95.712):

		self.ACT_LEVEL = lvl
		self.EXP = exp
		self.FORMULA = formula
		self.TO_NEXT_LEVEL= int(self.FORMULA*(lvl+1))
		self.TOTAL_EXP = exp
		self.MAX_LEVEL = 99

	def set_to_next_level(self):
		self.TO_NEXT_LEVEL = int(self.FORMULA*(self.ACT_LEVEL+1))

	def sum_exp(self, exp):
		print("you got " + str(exp) + " points of experience")
		if self.ACT_LEVEL < self.MAX_LEVEL:
			self.EXP += exp
			self.level_up()
			print("act exp " +str(self.EXP))

	def level_up(self): 

		if self.EXP > self.TO_NEXT_LEVEL:
			print("you went to level " + str(self.ACT_LEVEL+1))
			self.ACT_LEVEL += 1
			self.EXP -= self.TO_NEXT_LEVEL

			self.set_to_next_level()
			if self.ACT_LEVEL < self.MAX_LEVEL:
				print("to next level: " + str(self.TO_NEXT_LEVEL))		
				self.level_up()



class ally():

	def __init__(self, name, job, sub_job):

		global JOB_LIST

		self.NAME = name
		self.STATS = stats(276, 190, 11, 19, 19, 19, 19, 19, 19, 93, 19, 1, 1)
		self.LEVEL = level()
		self.ELEMENTAL_RESISTANCE = elemental_resistance(0,0,0,0,0,0,0,0)
		self.JOB = job
		self.SUB_JOB = sub_job
		self.STATS.modify_aptitudes(self.JOB.STATS_APTITUDE)
		self.BP = 0

		self.CURRENT_HP = self.STATS.HP
		self.CURRENT_MP = self.STATS.MP

		self.PASSIVES = []

		self.LEFT_HAND = -1
		self.RIGHT_HAND = -1
		self.HEAD = -1
		self.ARMOR = -1
		self.ACCESSORY_1 = -1
		self.ACCESSORY_2 = -1

	def change_job(self, job, sub_job):

		self.JOB = job
		self.SUB_JOB = sub_job
		self.STATS.modify_aptitudes(JOB_LIST[self.JOB].STATS_APTITUDE)

		if self.CURRENT_MP > self.STATS.MP:
			self.CURRENT_MP = self.STATS.MP
		if self.CURRENT_HP > self.STATS.HP:
			self.CURRENT_HP = self.STATS.HP

	def gain_exp(self, exp):

		xp = self.LEVEL.ACT_LEVEL
		self.LEVEL.sum_exp(exp)
		if self.LEVEL.ACT_LEVEL != xp:
			self.STATS.modify_by_level(self.LEVEL.ACT_LEVEL, JOB_LIST[self.JOB].STATS_APTITUDE)






class Cera(ally):

	def __init__(self, job, sub_job):

		super().__init__("Cera", job, sub_job)

class Noam(ally):

	def __init__(self, job, sub_job):

		super().__init__("Noam", job, sub_job)

class Andy(ally):

	def __init__(self, job, sub_job):

		super().__init__("Andy", job, sub_job)

class Lucille(ally):

	def __init__(self, job, sub_job):

		super().__init__("Lucille", job, sub_job)



class job():

	def __init__(self,name, stats_aptitude, weapon_armor_aptitude):
		self.NAME = name
		self.STATS_APTITUDE = []
		self.WEAPON_ARMOR_APTITUDE = []

		for i in range(len(stats_aptitude)):
			self.STATS_APTITUDE.append(stats_aptitude[i])
		for i in range(len(weapon_armor_aptitude)):
			self.WEAPON_ARMOR_APTITUDE.append(weapon_armor_aptitude[i])

		self.LEVEL_CERA = level(1,0,100)
		self.LEVEL_NOAM = level(1,0,100)
		self.LEVEL_ANDY = level(1,0,100)
		self.LEVEL_LUCILLE = level(1,0,100)


#Display data (this must be in a csv later)

FREELANCER_STATS_APTITUDE = ["C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C"]
FREELANCER_WEAPON_ARMOR_APTITUDE = ["C", "C", "C", "C", "C", "C", "C", "B", "C", "C", "C"]
FREELANCER = job("Freelancer", FREELANCER_STATS_APTITUDE, FREELANCER_WEAPON_ARMOR_APTITUDE)

WHITE_MAGE_STATS_APTITUDE = ["C", "A", "D", "D", "C", "B", "A", "S", "C", "C", "C", "B", "D"]
WHITE_MAGE_WEAPON_ARMOR_APTITUDE = ["E", "E", "C", "E", "C", "C", "A", "D", "B", "D", "A"]
WHITE_MAGE = job("White Mage", WHITE_MAGE_STATS_APTITUDE, WHITE_MAGE_WEAPON_ARMOR_APTITUDE)

JOB_LIST.append(FREELANCER)
JOB_LIST.append(WHITE_MAGE)
