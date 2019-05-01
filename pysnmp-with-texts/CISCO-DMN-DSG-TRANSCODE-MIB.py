#
# PySNMP MIB module CISCO-DMN-DSG-TRANSCODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-TRANSCODE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Integer32, MibIdentifier, Gauge32, NotificationType, ObjectIdentity, Counter32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibIdentifier", "Gauge32", "NotificationType", "ObjectIdentity", "Counter32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGTranscode = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37))
ciscoDSGTranscode.setRevisions(('2013-07-10 12:20', '2012-03-20 18:00', '2010-10-13 08:00', '2010-08-24 07:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGTranscode.setRevisionsDescriptions(('V01.00.04 2013-07-10 Remove slv(34) from transcoderSubtLangList.', 'V01.00.03 2012-03-18 Updated for D9854 R4 release.', 'V01.00.02 2010-10-31 Updated enum values for transcoderCfgManualGOP transcoderCfgSDHRes and transcoderCfgSDManualGOP.', 'V01.00.00 2010-08-24 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGTranscode.setLastUpdated('201307101220Z')
if mibBuilder.loadTexts: ciscoDSGTranscode.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGTranscode.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGTranscode.setDescription('Cisco Transcode MIB.')
transcoderInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 1))
transcoderTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2))
transcoderLOIAction = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("blackOutput", 1), ("noOutput", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderLOIAction.setStatus('current')
if mibBuilder.loadTexts: transcoderLOIAction.setDescription('Select whether outputs should transmit black or not transmit any data when there is a loss of input.')
transcoderCfgTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1), )
if mibBuilder.loadTexts: transcoderCfgTable.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgTable.setDescription('Transcoder Configuration Table.')
transcoderCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-TRANSCODE-MIB", "transcoderCfgIndex"))
if mibBuilder.loadTexts: transcoderCfgEntry.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgEntry.setDescription('Entry for Transcoder configuration table.')
transcoderCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transcoderCfgIndex.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgIndex.setDescription('Transcoder index.')
transcoderCfgApplyInband = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgApplyInband.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgApplyInband.setDescription('Apply in band transcoder parameters.')
transcoderCfgVRes = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 5))).clone(namedValues=NamedValues(("auto", 1), ("hdOut", 4), ("sdOut", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgVRes.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgVRes.setDescription('Selection for Vertical resolution.')
transcoderCfgCCPkt1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ccCEA708", 2), ("ccSCTE20", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgCCPkt1.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgCCPkt1.setDescription('Transcode Closed Caption Packet 1.')
transcoderCfgCCPkt2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ccCEA708", 2), ("ccSCTE20", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgCCPkt2.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgCCPkt2.setDescription('Transcode Closed Caption Packet 2.')
transcoderCfgCCPkt3 = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ccCEA708", 2), ("ccSCTE20", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transcoderCfgCCPkt3.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgCCPkt3.setDescription('Transcode Closed Caption Packet 3.')
transcoderCfgPCRRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transcoderCfgPCRRate.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgPCRRate.setDescription('PCR insertion rate in milliseconds.')
transcoderCfgHDHRes = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1440, 1920))).clone(namedValues=NamedValues(("threeQuarter", 1440), ("full", 1920)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgHDHRes.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgHDHRes.setDescription('High Definition Horizontal Resolution.')
transcoderCfgHDBitrateMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cbr", 1), ("vbr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgHDBitrateMode.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgHDBitrateMode.setDescription('HD Bit rate mode selection : Constant Bit Rate( cbr )/ Variable Bit Rate ( vbr ).')
transcoderCfgHDBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(8000000, 25000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgHDBitRate.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgHDBitRate.setDescription('HD bit rate in steps of 400bps. The Lower Limit is 8Mbps for D9859 and 10Mbps for D9858.')
transcoderCfgHDGOP = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("iFrameSync", 1), ("userGop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgHDGOP.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgHDGOP.setDescription('HD GOP selection.')
transcoderCfgHDManualGOP = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(10, 122, 152, 242, 302))).clone(namedValues=NamedValues(("manualGOP10", 10), ("manualGOP122", 122), ("manualGOP152", 152), ("manualGOP242", 242), ("manualGOP302", 302)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgHDManualGOP.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgHDManualGOP.setDescription('HD Manual GOP selection.')
transcoderCfgHD32PullDown = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgHD32PullDown.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgHD32PullDown.setDescription('3-2 Pulldown enabling.')
transcoderCfgHDAspectRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fourThird", 1), ("sixteenNinth", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transcoderCfgHDAspectRatio.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgHDAspectRatio.setDescription('HD Output Aspect ratio.')
transcoderCfgHDARConversion = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 1), ("auto", 2), ("autoAFD", 3), ("fourByThreeLetterBox", 4), ("fourByThreePillarBox", 5), ("fourteenByNine", 6), ("fourByThreeFullHeight", 7), ("sixteenByNineFullWidth", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transcoderCfgHDARConversion.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgHDARConversion.setDescription('HD Aspect ratio conversion.')
transcoderCfgHDVideoPreproc = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("deBlock", 2), ("mosquito", 3), ("edgeEnhancement", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transcoderCfgHDVideoPreproc.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgHDVideoPreproc.setDescription('Transcode HD Video Pre-processing.')
transcoderCfgSDHRes = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(352, 480, 528, 544, 704, 720))).clone(namedValues=NamedValues(("threeHundredAndFiftyTwo", 352), ("fourHundredAndEighty", 480), ("fiveHundredAndTwentyEight", 528), ("fiveHundredAndFourtyFour", 544), ("sevenHundredAndFour", 704), ("sevenHundredAndTwenty", 720)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgSDHRes.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgSDHRes.setDescription('Standard Definition Horizontal Resolution.')
transcoderCfgSDBitRateMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cbr", 1), ("vbr", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgSDBitRateMode.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgSDBitRateMode.setDescription('Transcode SD bit rate mode : Constant Bit Rate mode ( cbr )/ Variable Bit Rate mode ( vbr ).')
transcoderCfgSDBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2000000, 15000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgSDBitRate.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgSDBitRate.setDescription('SD Bit rate in steps of 400.')
transcoderCfgSDGOP = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("iFrameSync", 1), ("userGOPmn", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgSDGOP.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgSDGOP.setDescription('Transcode SD Group of Pictures-Format : Transparent/ Manual.')
transcoderCfgSDManualGOP = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(10, 122, 152, 242, 302))).clone(namedValues=NamedValues(("manualgop10", 10), ("manualgop122", 122), ("manualgop152", 152), ("manualgop242", 242), ("manualgop302", 302)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgSDManualGOP.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgSDManualGOP.setDescription('Transcode SD Manual Group of Pictures - Format values.')
transcoderCfgSD32PullDown = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgSD32PullDown.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgSD32PullDown.setDescription('Transcode SD 3:2 Pulldown: Enabled/ disabled.')
transcoderCfgSDAspectRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fourThird", 1), ("sixteenNinth", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgSDAspectRatio.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgSDAspectRatio.setDescription('Transcode SD Aspect ratio.')
transcoderCfgSDARConversion = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 1), ("auto", 2), ("autoAFD", 3), ("fourByThreeLetterBox", 4), ("fourByThreePillarBox", 5), ("fourteenByNine", 6), ("fourByThreeFullHeight", 7), ("sixteenByNineFullWidth", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderCfgSDARConversion.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgSDARConversion.setDescription('Transcode SD Aspect ratio conversion.')
transcoderCfgSDVideoPreproc = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("deBlock", 2), ("mosquito", 3), ("edgeEnhancement", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transcoderCfgSDVideoPreproc.setStatus('current')
if mibBuilder.loadTexts: transcoderCfgSDVideoPreproc.setDescription('Transcode SD Video Pre-processing.')
transcoderStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 2), )
if mibBuilder.loadTexts: transcoderStatusTable.setStatus('current')
if mibBuilder.loadTexts: transcoderStatusTable.setDescription('Transcoder status Table.')
transcoderStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-TRANSCODE-MIB", "transcoderStatusIndex"))
if mibBuilder.loadTexts: transcoderStatusEntry.setStatus('current')
if mibBuilder.loadTexts: transcoderStatusEntry.setDescription('Entry for transcoder status table.')
transcoderStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transcoderStatusIndex.setStatus('current')
if mibBuilder.loadTexts: transcoderStatusIndex.setDescription('Trancoder status index.')
transcoderStatusVideoStream = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("unknown", 1), ("sd480i2997", 2), ("sd480i3000", 3), ("sd576i2500", 4), ("hd720p5000", 5), ("hd720p5994", 6), ("hd720p6000", 7), ("hd1080i2500", 8), ("hd1080i2997", 9), ("hd1080i3000", 10), ("unsupported", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transcoderStatusVideoStream.setStatus('current')
if mibBuilder.loadTexts: transcoderStatusVideoStream.setDescription('Incoming stream format.')
transcoderSubtTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3), )
if mibBuilder.loadTexts: transcoderSubtTable.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtTable.setDescription('Transcoder Subtitle Table.')
transcoderSubtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1), ).setIndexNames((0, "CISCO-DMN-DSG-TRANSCODE-MIB", "transcoderSubtIndex"))
if mibBuilder.loadTexts: transcoderSubtEntry.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtEntry.setDescription('Entry for transcoder subtitle burn-in table.')
transcoderSubtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transcoderSubtIndex.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtIndex.setDescription('Trancoder subtitle burn-in index.')
transcoderSubtOpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("imiText", 3), ("dvb", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderSubtOpMode.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtOpMode.setDescription('Subtitle Burn-In Subtitles Mode: On/Off/Imitext/DVB.')
transcoderSubtLangMenu = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("languageList", 1), ("languageEntry", 2), ("pmtOrder", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderSubtLangMenu.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtLangMenu.setDescription('Subtitle Burn-In Language Preference by Language List, PMT Order or Manual Entry.')
transcoderSubtLangList = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43))).clone(namedValues=NamedValues(("ara", 1), ("btk", 2), ("ben", 3), ("bul", 4), ("chi", 5), ("cze", 6), ("dan", 7), ("dut", 8), ("eng", 9), ("fin", 10), ("fre", 11), ("ger", 12), ("gre", 13), ("heb", 14), ("hin", 15), ("hun", 16), ("ice", 17), ("ind", 18), ("ita", 19), ("jpn", 20), ("kor", 21), ("may", 22), ("mul", 23), ("nor", 24), ("per", 25), ("pol", 26), ("por", 27), ("rum", 28), ("rus", 29), ("san", 30), ("scc", 31), ("sin", 32), ("slo", 33), ("som", 35), ("spa", 36), ("swe", 37), ("tai", 38), ("tam", 39), ("tha", 40), ("tur", 41), ("ukr", 42), ("vie", 43)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderSubtLangList.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtLangList.setDescription('Subtitle Burn-In MPEG Languages Codes from the Language List.')
transcoderSubtPMTOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("first", 1), ("second", 2), ("third", 3), ("fourth", 4), ("fifth", 5), ("sixth", 6), ("seventh", 7), ("eighth", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderSubtPMTOrder.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtPMTOrder.setDescription('Subtitle Burn-In For Multiple Subtitle PIDs Select 1st, 2nd, 3rd, etc.')
transcoderSubtManualEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderSubtManualEntry.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtManualEntry.setDescription('Subtitle Burn-In Preferred Language Code.')
transcoderSubtImitextPos = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("extended", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderSubtImitextPos.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtImitextPos.setDescription('Subtitle Burn-In Imitext Positioning: Standard/Extended.')
transcoderSubtForeGround = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("yellow", 2), ("white", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderSubtForeGround.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtForeGround.setDescription('Subtitle Burn-In Imitext Foreground Colour: Yellow/White/Auto.')
transcoderSubtBackGround = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("auto", 2), ("shadow", 3), ("opaque", 4), ("semi", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transcoderSubtBackGround.setStatus('current')
if mibBuilder.loadTexts: transcoderSubtBackGround.setDescription('Subtitle Burn-In Imitext Background Colour: None/Auto/Shadow/Opaque/Semi.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-TRANSCODE-MIB", transcoderCfgCCPkt1=transcoderCfgCCPkt1, transcoderCfgCCPkt3=transcoderCfgCCPkt3, transcoderSubtOpMode=transcoderSubtOpMode, transcoderSubtLangList=transcoderSubtLangList, transcoderSubtImitextPos=transcoderSubtImitextPos, transcoderCfgSDAspectRatio=transcoderCfgSDAspectRatio, transcoderCfgSDHRes=transcoderCfgSDHRes, transcoderCfgIndex=transcoderCfgIndex, transcoderCfgSDBitRateMode=transcoderCfgSDBitRateMode, transcoderStatusEntry=transcoderStatusEntry, transcoderStatusIndex=transcoderStatusIndex, transcoderCfgVRes=transcoderCfgVRes, transcoderInfo=transcoderInfo, transcoderSubtEntry=transcoderSubtEntry, transcoderCfgHDManualGOP=transcoderCfgHDManualGOP, transcoderTable=transcoderTable, transcoderSubtBackGround=transcoderSubtBackGround, transcoderCfgHDAspectRatio=transcoderCfgHDAspectRatio, transcoderCfgHDVideoPreproc=transcoderCfgHDVideoPreproc, transcoderCfgSDManualGOP=transcoderCfgSDManualGOP, transcoderStatusTable=transcoderStatusTable, transcoderSubtPMTOrder=transcoderSubtPMTOrder, transcoderSubtLangMenu=transcoderSubtLangMenu, transcoderCfgHDGOP=transcoderCfgHDGOP, transcoderCfgCCPkt2=transcoderCfgCCPkt2, transcoderCfgHD32PullDown=transcoderCfgHD32PullDown, ciscoDSGTranscode=ciscoDSGTranscode, transcoderSubtIndex=transcoderSubtIndex, transcoderCfgApplyInband=transcoderCfgApplyInband, transcoderCfgHDBitrateMode=transcoderCfgHDBitrateMode, transcoderCfgSDVideoPreproc=transcoderCfgSDVideoPreproc, transcoderCfgPCRRate=transcoderCfgPCRRate, transcoderCfgTable=transcoderCfgTable, transcoderCfgEntry=transcoderCfgEntry, transcoderCfgHDHRes=transcoderCfgHDHRes, transcoderSubtTable=transcoderSubtTable, transcoderCfgHDARConversion=transcoderCfgHDARConversion, transcoderCfgSDBitRate=transcoderCfgSDBitRate, transcoderSubtForeGround=transcoderSubtForeGround, transcoderStatusVideoStream=transcoderStatusVideoStream, transcoderSubtManualEntry=transcoderSubtManualEntry, PYSNMP_MODULE_ID=ciscoDSGTranscode, transcoderCfgSD32PullDown=transcoderCfgSD32PullDown, transcoderLOIAction=transcoderLOIAction, transcoderCfgSDGOP=transcoderCfgSDGOP, transcoderCfgHDBitRate=transcoderCfgHDBitRate, transcoderCfgSDARConversion=transcoderCfgSDARConversion)
