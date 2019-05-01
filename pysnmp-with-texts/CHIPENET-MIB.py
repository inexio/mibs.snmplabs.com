#
# PySNMP MIB module CHIPENET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CHIPENET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:48:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
DisplayString, = mibBuilder.importSymbols("RFC1155-SMI", "DisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, IpAddress, Counter32, iso, enterprises, Gauge32, Counter64, Integer32, ObjectIdentity, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "IpAddress", "Counter32", "iso", "enterprises", "Gauge32", "Counter64", "Integer32", "ObjectIdentity", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chipcom = MibIdentifier((1, 3, 6, 1, 4, 1, 49))
chipmib02 = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2))
chipGen = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 1))
chipEcho = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 2))
chipProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3))
chipExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 4))
chipTTY = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 5))
chipTFTP = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 6))
chipDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 7))
online = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1))
oebm = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 2))
midnight = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 3))
workGroupHub = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 4))
emm = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 5))
chipBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 6))
trmm = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 7))
fmm = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 8))
focus1 = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 9))
oeim = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 10))
chipExpTokenRing = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 4, 1))
dot1dBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 4, 14))
dot5 = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1))
olAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1))
olConc = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2))
olEnv = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3))
olModules = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4))
olNets = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5))
olGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6))
olAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7))
olSpecMods = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4))
ol50nnMCTL = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3))
ol51nnMMGT = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4))
ol51nnMFIB = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5))
ol51nnMUTP = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6))
ol51nnMTP = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7))
ol51nnMBNC = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8))
ol51nnBEE = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9))
ol51nnRES = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10))
ol51nnREE = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11))
ol51nnMAUIF = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12))
ol51nnMAUIM = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13))
ol5208MTP = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14))
ol51nnMFP = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15))
ol51nnMFBP = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16))
ol51nnMTPL = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17))
ol51nnMTPPL = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18))
ol52nnMTP = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19))
ol52nnMFR = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20))
ol51nnMTS = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21))
ol51nnMFL = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22))
ol50nnMRCTL = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23))
ol51nnMFB = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24))
ol53nnMMGT = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25))
ol53nnMFBMIC = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26))
ol53nnMFIBST = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27))
ol53nnMSTP = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28))
ol51nnMTPCL = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29))
ol52nnBTT = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30))
ol51nnIx = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31))
ol52nnMMGT = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32))
ol50nnMHCTL = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33))
olNet = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1))
olEnet = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2))
olTRnet = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3))
olFDDInet = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4))
hubSysGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 1))
hardwareGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 2))
softwareGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 3))
hubGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 4))
boardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 5))
portGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 6))
alarmGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 7))
olThresh = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1))
olThreshControl = MibIdentifier((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1))
olEnetStatsTable = MibTable((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1), )
if mibBuilder.loadTexts: olEnetStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsTable.setDescription('A table that contains statistical information about Ethernet (IEEE 802.3) networks.')
olEnetStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1), ).setIndexNames((0, "CHIPENET-MIB", "olEnetStatsNetID"))
if mibBuilder.loadTexts: olEnetStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsEntry.setDescription('A list of statistical information about each Ethernet (IEEE 802.3) network in the concentrator.')
olEnetStatsNetID = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 7, 8))).clone(namedValues=NamedValues(("ethernet-1", 6), ("ethernet-2", 7), ("ethernet-3", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsNetID.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsNetID.setDescription('The network index that uniquely identifies this network. One of ethernet-1, ethernet-2, or ethernet-3.')
olEnetStatsFramesRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsFramesRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsFramesRcvdOks.setDescription('The count of frames that were successfully received by this network. This counter does not include frames received in error.')
olEnetStatsOctetsRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsOctetsRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsOctetsRcvdOks.setDescription('The count of the number of octets that were successfully received by this network. This counter does not include octets that were part of frames that were received in error.')
olEnetStatsMcastRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsMcastRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsMcastRcvdOks.setDescription('The count of the number of multicast frames successfully received by this network.')
olEnetStatsBcastRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsBcastRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsBcastRcvdOks.setDescription('The count of the number of broadcast frames successfully received by this network.')
olEnetStatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsFrameTooLongs.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsFrameTooLongs.setDescription('The count of the number of frames received by this network that exceeds the maximum permitted Ethernet (802.3) frame size.')
olEnetStatsAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsAlignmentErrors.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsAlignmentErrors.setDescription('The count of the number of frames received by this network that did not pass the frame check sequence (FCS) check and that are not an integral number of octets. These frames are not counted in olEnetStatsFCSErrors.')
olEnetStatsFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsFCSErrors.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsFCSErrors.setDescription('The count of the number of frames received by this network that did not pass the frame check sequence (FCS) check and are an integral number of octets.')
olEnetStatsRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsRunts.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsRunts.setDescription('The count of the number of frames received by this network that are less than 512 bits long. ')
olEnetStatsLocalColls = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsLocalColls.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsLocalColls.setDescription('The count of the number of times that two or more ports within this concentrator have received traffic simultaneously.')
olEnetStatsModTable = MibTable((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2), )
if mibBuilder.loadTexts: olEnetStatsModTable.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModTable.setDescription('A table of statistical information counted for each module in each Ethernet (IEEE 802.3) network.')
olEnetStatsModEntry = MibTableRow((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1), ).setIndexNames((0, "CHIPENET-MIB", "olEnetStatsModNetID"), (0, "CHIPENET-MIB", "olEnetStatsModSlotIndex"))
if mibBuilder.loadTexts: olEnetStatsModEntry.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModEntry.setDescription('A list of statistical information for each port on each Ethernet (IEEE 802.3) network in the concentrator.')
olEnetStatsModNetID = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 7, 8))).clone(namedValues=NamedValues(("ethernet-1", 6), ("ethernet-2", 7), ("ethernet-3", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsModNetID.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModNetID.setDescription('The unique identifier for this network. One of ethernet-1, ethernet-2, or ethernet-3.')
olEnetStatsModSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsModSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModSlotIndex.setDescription('The slot number that contains this module.')
olEnetStatsModFramesRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsModFramesRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModFramesRcvdOks.setDescription('The count of frames that were successfully received by this module. This counter does not include frames received in error.')
olEnetStatsModOctetsRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsModOctetsRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModOctetsRcvdOks.setDescription('The count of the number of octets that were successfully received by this module. This counter does not include octets that were part of frames that were received in error.')
olEnetStatsModMcastRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsModMcastRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModMcastRcvdOks.setDescription('The count of the number of multicast frames successfully received by this module.')
olEnetStatsModBcastRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsModBcastRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModBcastRcvdOks.setDescription('The count of the number of broadcast frames successfully received by this module.')
olEnetStatsModFrameTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsModFrameTooLongs.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModFrameTooLongs.setDescription('The count of the number of frames received by this module that exceeds the maximum permitted Ethernet (802.3) frame size.')
olEnetStatsModAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsModAlignmentErrors.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModAlignmentErrors.setDescription('The count of the number of frames received by this module that did not pass the frame check sequence (FCS) check and that are not an integral number of octets. These frames are not counted in olEnetStatsModFCSErrors.')
olEnetStatsModFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsModFCSErrors.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModFCSErrors.setDescription('The count of the number of frames received by this module that did not pass the frame check sequence (FCS) check and are an integral number of octets.')
olEnetStatsModRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsModRunts.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsModRunts.setDescription('The count of the number of frames received by this module that are less than 512 bits long. ')
olEnetStatsPortTable = MibTable((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3), )
if mibBuilder.loadTexts: olEnetStatsPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortTable.setDescription('A table of statistical information counted for each port in each Ethernet (IEEE 802.3) network.')
olEnetStatsPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1), ).setIndexNames((0, "CHIPENET-MIB", "olEnetStatsPortSlotIndex"), (0, "CHIPENET-MIB", "olEnetStatsPortIndex"))
if mibBuilder.loadTexts: olEnetStatsPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortEntry.setDescription('A list of statistical information for each port on each Ethernet (IEEE 802.3) network in the concentrator.')
olEnetStatsPortNetID = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 7, 8))).clone(namedValues=NamedValues(("ethernet-1", 6), ("ethernet-2", 7), ("ethernet-3", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortNetID.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortNetID.setDescription('The unique identifier for this network. One of ethernet-1, ethernet-2, or ethernet-3.')
olEnetStatsPortSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortSlotIndex.setDescription('The slot number that contains this port.')
olEnetStatsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortIndex.setDescription('The port number within this slot.')
olEnetStatsPortFramesRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortFramesRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortFramesRcvdOks.setDescription('The count of frames that were successfully received by this port. This counter does not include frames received in error.')
olEnetStatsPortOctetsRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortOctetsRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortOctetsRcvdOks.setDescription('The count of the number of octets that were successfully received by this port. This counter does not include octets that were part of frames that were received in error.')
olEnetStatsPortMcastRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortMcastRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortMcastRcvdOks.setDescription('The count of the number of multicast frames successfully received by this port.')
olEnetStatsPortBcastRcvdOks = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortBcastRcvdOks.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortBcastRcvdOks.setDescription('The count of the number of broadcast frames successfully received by this port.')
olEnetStatsPortFrameTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortFrameTooLongs.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortFrameTooLongs.setDescription('The count of the number of frames received by this port that exceeds the maximum permitted Ethernet (802.3) frame size.')
olEnetStatsPortAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortAlignmentErrors.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortAlignmentErrors.setDescription('The count of the number of frames received by this port that did not pass the frame check sequence (FCS) check and that are not an integral number of octets. These frames are not counted in olEnetStatsPortFCSErrors.')
olEnetStatsPortFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortFCSErrors.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortFCSErrors.setDescription('The count of the number of frames received by this port that did not pass the frame check sequence (FCS) check and are an integral number of octets.')
olEnetStatsPortRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortRunts.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortRunts.setDescription('The count of the number of frames received by this port that are less than 512 bits long. ')
olEnetStatsPortSrcAddrChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortSrcAddrChanges.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortSrcAddrChanges.setDescription('The count of the number of times that olEnetStatsPortLastSourceAddr { olEnetStatsPortEntry 11 } has changed.')
olEnetStatsPortLastSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortLastSrcAddr.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortLastSrcAddr.setDescription('The last source address seen on this port for this network for the last successfully received frame.')
olEnetStatsPortLastErrAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 3, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetStatsPortLastErrAddr.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetStatsPortLastErrAddr.setDescription('The value stored in the source address portion of a frame received in error (alignment, FCS, or too long). Since the frame was received in error, there is no guarantee that this is an actual valid address.')
olEnetMapTable = MibTable((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4), )
if mibBuilder.loadTexts: olEnetMapTable.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetMapTable.setDescription("A table that contains a cache of information relating an Ethernet source address with a specific port for a given network. An indication of this source's utilization of the network is also provided.")
olEnetMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1), ).setIndexNames((0, "CHIPENET-MIB", "olEnetMapNetID"), (0, "CHIPENET-MIB", "olEnetMapAddress"))
if mibBuilder.loadTexts: olEnetMapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetMapEntry.setDescription('A list of information that tracks a source address to a specific port for each network.')
olEnetMapNetID = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(6, 7, 8))).clone(namedValues=NamedValues(("ethernet-1", 6), ("ethernet-2", 7), ("ethernet-3", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetMapNetID.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetMapNetID.setDescription('The network index that uniquely identifies this network. One of ethernet-1, ethernet-2, ethernet-3.')
olEnetMapAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetMapAddress.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetMapAddress.setDescription('An Ethernet source address received by this port on this network.')
olEnetMapSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetMapSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetMapSlotIndex.setDescription('The slot number of the port that received this address.')
olEnetMapPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetMapPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetMapPortIndex.setDescription("The port number within olEnetMapSlotIndex's slot that received this address.")
olEnetMapFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetMapFrames.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetMapFrames.setDescription('An estimated count of the number of frames generated by this address. This count should be interpreted as an indicator, not a true frame count.')
olEnetMapOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetMapOctets.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetMapOctets.setDescription('An estimated count of the number of octets generated by this address. This count should be interpreted as an indicator, not a true octet count.')
olEnetMapTime = MibTableColumn((1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: olEnetMapTime.setStatus('mandatory')
if mibBuilder.loadTexts: olEnetMapTime.setDescription('The time in in hundredths of a second since this address was last seen. For example, if olEnetMapTime is 500 ticks, then this adddress was seen 5 seconds ago.')
mibBuilder.exportSymbols("CHIPENET-MIB", ol51nnMAUIM=ol51nnMAUIM, ol52nnMFR=ol52nnMFR, ol51nnMTPCL=ol51nnMTPCL, olFDDInet=olFDDInet, ol51nnIx=ol51nnIx, olEnetStatsModEntry=olEnetStatsModEntry, olAgents=olAgents, olEnetStatsFramesRcvdOks=olEnetStatsFramesRcvdOks, ol52nnMTP=ol52nnMTP, chipEcho=chipEcho, olEnetStatsPortSrcAddrChanges=olEnetStatsPortSrcAddrChanges, chipExperiment=chipExperiment, olEnetMapAddress=olEnetMapAddress, ol50nnMRCTL=ol50nnMRCTL, ol50nnMCTL=ol50nnMCTL, ol51nnMFP=ol51nnMFP, olEnetStatsPortRunts=olEnetStatsPortRunts, olNets=olNets, olEnetStatsPortTable=olEnetStatsPortTable, olEnet=olEnet, chipmib02=chipmib02, olEnetMapTime=olEnetMapTime, olEnetStatsLocalColls=olEnetStatsLocalColls, emm=emm, olEnetMapPortIndex=olEnetMapPortIndex, chipTTY=chipTTY, ol51nnBEE=ol51nnBEE, olEnetStatsAlignmentErrors=olEnetStatsAlignmentErrors, olEnetStatsPortOctetsRcvdOks=olEnetStatsPortOctetsRcvdOks, olEnetStatsPortIndex=olEnetStatsPortIndex, ol52nnBTT=ol52nnBTT, olEnetStatsModTable=olEnetStatsModTable, ol51nnREE=ol51nnREE, ol51nnMUTP=ol51nnMUTP, olEnetStatsOctetsRcvdOks=olEnetStatsOctetsRcvdOks, olAlarm=olAlarm, dot5=dot5, olEnetStatsBcastRcvdOks=olEnetStatsBcastRcvdOks, ol51nnRES=ol51nnRES, ol53nnMSTP=ol53nnMSTP, online=online, boardGroup=boardGroup, olEnetMapTable=olEnetMapTable, ol51nnMFL=ol51nnMFL, workGroupHub=workGroupHub, olEnv=olEnv, chipExpTokenRing=chipExpTokenRing, olEnetStatsPortLastSrcAddr=olEnetStatsPortLastSrcAddr, olThreshControl=olThreshControl, olEnetStatsPortNetID=olEnetStatsPortNetID, olEnetStatsModOctetsRcvdOks=olEnetStatsModOctetsRcvdOks, focus1=focus1, ol53nnMMGT=ol53nnMMGT, olEnetStatsTable=olEnetStatsTable, oebm=oebm, midnight=midnight, olSpecMods=olSpecMods, olEnetStatsPortMcastRcvdOks=olEnetStatsPortMcastRcvdOks, olEnetStatsPortBcastRcvdOks=olEnetStatsPortBcastRcvdOks, olNet=olNet, olEnetMapSlotIndex=olEnetMapSlotIndex, olEnetStatsPortFrameTooLongs=olEnetStatsPortFrameTooLongs, ol51nnMFIB=ol51nnMFIB, olEnetStatsNetID=olEnetStatsNetID, chipcom=chipcom, olEnetStatsPortFCSErrors=olEnetStatsPortFCSErrors, hardwareGroup=hardwareGroup, hubGroup=hubGroup, olEnetStatsModAlignmentErrors=olEnetStatsModAlignmentErrors, olEnetStatsMcastRcvdOks=olEnetStatsMcastRcvdOks, ol51nnMTPPL=ol51nnMTPPL, olEnetMapFrames=olEnetMapFrames, olEnetStatsModSlotIndex=olEnetStatsModSlotIndex, olEnetStatsPortFramesRcvdOks=olEnetStatsPortFramesRcvdOks, olTRnet=olTRnet, olEnetMapNetID=olEnetMapNetID, ol51nnMTS=ol51nnMTS, olEnetStatsModFrameTooLongs=olEnetStatsModFrameTooLongs, softwareGroup=softwareGroup, trmm=trmm, ol51nnMTP=ol51nnMTP, olModules=olModules, olEnetStatsModRunts=olEnetStatsModRunts, olEnetStatsEntry=olEnetStatsEntry, dot1dBridge=dot1dBridge, chipBridge=chipBridge, ol51nnMTPL=ol51nnMTPL, olConc=olConc, olEnetMapEntry=olEnetMapEntry, ol50nnMHCTL=ol50nnMHCTL, chipTFTP=chipTFTP, olEnetStatsModFCSErrors=olEnetStatsModFCSErrors, olEnetStatsModBcastRcvdOks=olEnetStatsModBcastRcvdOks, olEnetStatsPortLastErrAddr=olEnetStatsPortLastErrAddr, fmm=fmm, ol5208MTP=ol5208MTP, olEnetStatsPortSlotIndex=olEnetStatsPortSlotIndex, olEnetMapOctets=olEnetMapOctets, hubSysGroup=hubSysGroup, olGroups=olGroups, ol51nnMBNC=ol51nnMBNC, ol52nnMMGT=ol52nnMMGT, alarmGroup=alarmGroup, ol51nnMAUIF=ol51nnMAUIF, olEnetStatsFrameTooLongs=olEnetStatsFrameTooLongs, olThresh=olThresh, olEnetStatsModNetID=olEnetStatsModNetID, chipDownload=chipDownload, ol53nnMFBMIC=ol53nnMFBMIC, ol53nnMFIBST=ol53nnMFIBST, oeim=oeim, ol51nnMMGT=ol51nnMMGT, portGroup=portGroup, ol51nnMFBP=ol51nnMFBP, olEnetStatsPortAlignmentErrors=olEnetStatsPortAlignmentErrors, chipProducts=chipProducts, ol51nnMFB=ol51nnMFB, olEnetStatsRunts=olEnetStatsRunts, olEnetStatsModFramesRcvdOks=olEnetStatsModFramesRcvdOks, olEnetStatsFCSErrors=olEnetStatsFCSErrors, olEnetStatsModMcastRcvdOks=olEnetStatsModMcastRcvdOks, chipGen=chipGen, olEnetStatsPortEntry=olEnetStatsPortEntry)
