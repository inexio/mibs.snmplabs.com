#
# PySNMP MIB module HH3C-IDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-IDS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, ObjectIdentity, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, Unsigned32, TimeTicks, IpAddress, ModuleIdentity, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "ObjectIdentity", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "Unsigned32", "TimeTicks", "IpAddress", "ModuleIdentity", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cIDSMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1))
if mibBuilder.loadTexts: hh3cIDSMib.setLastUpdated('200507141942Z')
if mibBuilder.loadTexts: hh3cIDSMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cIds = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 47))
hh3cIDSTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1))
hh3cIDSTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1))
hh3cIDSTrapIPFragmentQueueLen = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapIPFragmentQueueLen.setStatus('current')
hh3cIDSTrapStatSessionTabLen = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapStatSessionTabLen.setStatus('current')
hh3cIDSTrapIPAddressType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapIPAddressType.setStatus('current')
hh3cIDSTrapIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 4), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapIPAddress.setStatus('current')
hh3cIDSTrapUserName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapUserName.setStatus('current')
hh3cIDSTrapLoginType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("telnet", 1), ("ssh", 2), ("web", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapLoginType.setStatus('current')
hh3cIDSTrapUpgradeType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("programme", 1), ("crb", 2), ("vrb", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapUpgradeType.setStatus('current')
hh3cIDSTrapCRLName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapCRLName.setStatus('current')
hh3cIDSTrapCertName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapCertName.setStatus('current')
hh3cIDSTrapDetectRuleID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 10), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapDetectRuleID.setStatus('current')
hh3cIDSTrapEngineID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 11), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapEngineID.setStatus('current')
hh3cIDSTrapFileName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapFileName.setStatus('current')
hh3cIDSTrapCfgLineInFile = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 13), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapCfgLineInFile.setStatus('current')
hh3cIDSTrapReasonForError = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cIDSTrapReasonForError.setStatus('current')
hh3cIDSTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2))
hh3cIDSTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0))
hh3cIDSTrapIPFragQueueFull = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 1)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapIPFragmentQueueLen"), ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapIPFragQueueFull.setStatus('current')
hh3cIDSTrapStatSessTabFull = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 2)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapStatSessionTabLen"), ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapStatSessTabFull.setStatus('current')
hh3cIDSTrapDetectRuleParseFail = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 3)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapDetectRuleID"), ("HH3C-IDS-MIB", "hh3cIDSTrapEngineID"), ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapDetectRuleParseFail.setStatus('current')
hh3cIDSTrapDBConnLost = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 4)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapIPAddressType"), ("HH3C-IDS-MIB", "hh3cIDSTrapIPAddress"), ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapDBConnLost.setStatus('current')
hh3cIDSTrapCRLNeedUpdate = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 5)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapCRLName"), ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapCRLNeedUpdate.setStatus('current')
hh3cIDSTrapCertOverdue = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 6)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapCertName"), ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapCertOverdue.setStatus('current')
hh3cIDSTrapTooManyLoginFail = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 7)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapUserName"), ("HH3C-IDS-MIB", "hh3cIDSTrapIPAddressType"), ("HH3C-IDS-MIB", "hh3cIDSTrapIPAddress"), ("HH3C-IDS-MIB", "hh3cIDSTrapLoginType"), ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapTooManyLoginFail.setStatus('current')
hh3cIDSTrapUpgradeError = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 8)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapUpgradeType"), ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapUpgradeError.setStatus('current')
hh3cIDSTrapFileAccessError = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 9)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapFileName"), ("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapFileAccessError.setStatus('current')
hh3cIDSTrapConsArithMemLow = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 10)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapConsArithMemLow.setStatus('current')
hh3cIDSTrapSSRAMOperFail = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 11)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapSSRAMOperFail.setStatus('current')
hh3cIDSTrapPacketProcessDisorder = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 12)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapReasonForError"))
if mibBuilder.loadTexts: hh3cIDSTrapPacketProcessDisorder.setStatus('current')
hh3cIDSTrapCfgFileFormatError = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 47, 1, 1, 2, 0, 13)).setObjects(("HH3C-IDS-MIB", "hh3cIDSTrapFileName"), ("HH3C-IDS-MIB", "hh3cIDSTrapCfgLineInFile"))
if mibBuilder.loadTexts: hh3cIDSTrapCfgFileFormatError.setStatus('current')
mibBuilder.exportSymbols("HH3C-IDS-MIB", hh3cIDSTrapIPAddress=hh3cIDSTrapIPAddress, hh3cIDSTrapReasonForError=hh3cIDSTrapReasonForError, hh3cIDSTrapInfo=hh3cIDSTrapInfo, hh3cIDSTrapCertOverdue=hh3cIDSTrapCertOverdue, hh3cIDSTrapStatSessionTabLen=hh3cIDSTrapStatSessionTabLen, hh3cIDSTrapUpgradeType=hh3cIDSTrapUpgradeType, hh3cIDSTrapIPFragQueueFull=hh3cIDSTrapIPFragQueueFull, hh3cIDSTrapCRLNeedUpdate=hh3cIDSTrapCRLNeedUpdate, hh3cIDSTrapCfgLineInFile=hh3cIDSTrapCfgLineInFile, hh3cIDSTrapEngineID=hh3cIDSTrapEngineID, PYSNMP_MODULE_ID=hh3cIDSMib, hh3cIds=hh3cIds, hh3cIDSTrapGroup=hh3cIDSTrapGroup, hh3cIDSTrapFileName=hh3cIDSTrapFileName, hh3cIDSTrapDetectRuleID=hh3cIDSTrapDetectRuleID, hh3cIDSTrapTooManyLoginFail=hh3cIDSTrapTooManyLoginFail, hh3cIDSTrapUpgradeError=hh3cIDSTrapUpgradeError, hh3cIDSTrapPrefix=hh3cIDSTrapPrefix, hh3cIDSTrapFileAccessError=hh3cIDSTrapFileAccessError, hh3cIDSTrapCRLName=hh3cIDSTrapCRLName, hh3cIDSTrapIPFragmentQueueLen=hh3cIDSTrapIPFragmentQueueLen, hh3cIDSTrapDBConnLost=hh3cIDSTrapDBConnLost, hh3cIDSTrap=hh3cIDSTrap, hh3cIDSTrapSSRAMOperFail=hh3cIDSTrapSSRAMOperFail, hh3cIDSTrapUserName=hh3cIDSTrapUserName, hh3cIDSTrapCertName=hh3cIDSTrapCertName, hh3cIDSTrapIPAddressType=hh3cIDSTrapIPAddressType, hh3cIDSMib=hh3cIDSMib, hh3cIDSTrapConsArithMemLow=hh3cIDSTrapConsArithMemLow, hh3cIDSTrapPacketProcessDisorder=hh3cIDSTrapPacketProcessDisorder, hh3cIDSTrapDetectRuleParseFail=hh3cIDSTrapDetectRuleParseFail, hh3cIDSTrapStatSessTabFull=hh3cIDSTrapStatSessTabFull, hh3cIDSTrapCfgFileFormatError=hh3cIDSTrapCfgFileFormatError, hh3cIDSTrapLoginType=hh3cIDSTrapLoginType)
