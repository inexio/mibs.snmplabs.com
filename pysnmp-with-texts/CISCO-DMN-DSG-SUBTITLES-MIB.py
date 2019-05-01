#
# PySNMP MIB module CISCO-DMN-DSG-SUBTITLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-SUBTITLES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, NotificationType, IpAddress, Counter64, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Integer32, Unsigned32, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "NotificationType", "IpAddress", "Counter64", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Integer32", "Unsigned32", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGSubtitle = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16))
ciscoDSGSubtitle.setRevisions(('2013-07-10 12:20', '2010-08-30 11:00', '2009-12-07 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGSubtitle.setRevisionsDescriptions(('V01.00.02 2013-07-10 Updated subtitlesLangList DESCRIPTION clause.', 'V01.00.01 2010-08-30 Updated for adherence to SNMPv2 format.', 'V01.00.00 2009-12-07 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGSubtitle.setLastUpdated('201307101220Z')
if mibBuilder.loadTexts: ciscoDSGSubtitle.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGSubtitle.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGSubtitle.setDescription('Cisco Subtitles MIB.')
subtitlesOPMode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("imiText", 3), ("dvb", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subtitlesOPMode.setStatus('current')
if mibBuilder.loadTexts: subtitlesOPMode.setDescription('Subtitles Mode: On/Off/Imitext/DVB.')
subtitlesLangMenu = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("languageList", 1), ("languageEntry", 2), ("pmtOrder", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subtitlesLangMenu.setStatus('current')
if mibBuilder.loadTexts: subtitlesLangMenu.setDescription('Language Preference by Language List, PMT Order or Manual Entry.')
subtitlesLangList = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43))).clone(namedValues=NamedValues(("ara", 1), ("btk", 2), ("ben", 3), ("bul", 4), ("chi", 5), ("cze", 6), ("dan", 7), ("dut", 8), ("eng", 9), ("fin", 10), ("fre", 11), ("ger", 12), ("gre", 13), ("heb", 14), ("hin", 15), ("hun", 16), ("ice", 17), ("ind", 18), ("ita", 19), ("jpn", 20), ("kor", 21), ("may", 22), ("mul", 23), ("nor", 24), ("per", 25), ("pol", 26), ("por", 27), ("rum", 28), ("rus", 29), ("san", 30), ("scc", 31), ("sin", 32), ("slo", 33), ("slv", 34), ("som", 35), ("spa", 36), ("swe", 37), ("tai", 38), ("tam", 39), ("tha", 40), ("tur", 41), ("ukr", 42), ("vie", 43)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subtitlesLangList.setStatus('current')
if mibBuilder.loadTexts: subtitlesLangList.setDescription('MPEG Languages Codes from the Language List. Language option slv(34) is only supported on D9865.')
subtitlesPMTOrder = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("first", 1), ("second", 2), ("third", 3), ("fourth", 4), ("fifth", 5), ("sixth", 6), ("seventh", 7), ("eighth", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subtitlesPMTOrder.setStatus('current')
if mibBuilder.loadTexts: subtitlesPMTOrder.setDescription('For Multiple Subtitle PIDs Select 1st, 2nd, 3rd, etc.')
subtitlesManualEntry = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subtitlesManualEntry.setStatus('current')
if mibBuilder.loadTexts: subtitlesManualEntry.setDescription('Preferred Language Code.')
subtitlesIMITextPos = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("extended", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subtitlesIMITextPos.setStatus('current')
if mibBuilder.loadTexts: subtitlesIMITextPos.setDescription('Imitext Positioning: Standard/Extended.')
subtitlesForeGround = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("yellow", 2), ("white", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subtitlesForeGround.setStatus('current')
if mibBuilder.loadTexts: subtitlesForeGround.setDescription('Imitext Foreground Colour: Yellow/White/Auto.')
subtitlesBackGround = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 16, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("auto", 2), ("shadow", 3), ("opaque", 4), ("semi", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: subtitlesBackGround.setStatus('current')
if mibBuilder.loadTexts: subtitlesBackGround.setDescription('Imitext Background Colour: None/Auto/Shadow/Opaque/Semi.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-SUBTITLES-MIB", subtitlesPMTOrder=subtitlesPMTOrder, ciscoDSGSubtitle=ciscoDSGSubtitle, subtitlesLangMenu=subtitlesLangMenu, subtitlesBackGround=subtitlesBackGround, subtitlesIMITextPos=subtitlesIMITextPos, subtitlesLangList=subtitlesLangList, PYSNMP_MODULE_ID=ciscoDSGSubtitle, subtitlesManualEntry=subtitlesManualEntry, subtitlesForeGround=subtitlesForeGround, subtitlesOPMode=subtitlesOPMode)
