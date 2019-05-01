#
# PySNMP MIB module RUCKUS-RADIO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-RADIO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:58:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ruckusCommonRadioModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonRadioModule")
RuckusRadioMode, RuckusCountryCode, RuckusRate = mibBuilder.importSymbols("RUCKUS-TC-MIB", "RuckusRadioMode", "RuckusCountryCode", "RuckusRate")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Integer32, NotificationType, ModuleIdentity, iso, ObjectIdentity, Unsigned32, Counter32, IpAddress, Bits, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Integer32", "NotificationType", "ModuleIdentity", "iso", "ObjectIdentity", "Unsigned32", "Counter32", "IpAddress", "Bits", "TimeTicks", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ruckusRadioMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1))
if mibBuilder.loadTexts: ruckusRadioMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusRadioMIB.setOrganization('Ruckus Wireless, Inc.')
if mibBuilder.loadTexts: ruckusRadioMIB.setContactInfo('Ruckus Wireless, Inc. Postal: 880 W Maude Ave Sunnyvale, CA 94085 USA EMail: support@ruckuswireless.com Phone: +1-650-265-4200')
if mibBuilder.loadTexts: ruckusRadioMIB.setDescription('Ruckus Radio mib')
ruckusRadioObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1))
ruckusRadioInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1))
ruckusRadioNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioNumber.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioNumber.setDescription('The number of radios present on this system.')
ruckusRadioTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2), )
if mibBuilder.loadTexts: ruckusRadioTable.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioTable.setDescription('Radio table.')
ruckusRadioEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ruckusRadioEntry.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioEntry.setDescription('Specifies each Radio entry.')
ruckusRadioMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("auto", 0), ("ieee802dot11g-only", 1), ("ieee802dot11b-only", 2), ("ieee802dot11ng", 3), ("ieee802dot11na", 4), ("ieee802dot11a-only", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusRadioMode.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioMode.setDescription('Specifies the radio mode.')
ruckusRadioCountry = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 2), RuckusCountryCode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusRadioCountry.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioCountry.setDescription('Specifies the country code.')
ruckusRadioBSSType = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("station", 1), ("master", 2), ("independent", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioBSSType.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioBSSType.setDescription('Specifies the bss type.')
ruckusRadioChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusRadioChannel.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioChannel.setDescription('Specifies the current operating channel. When 0, it indicates the system selects the best channel automatically.')
ruckusRadioDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioDataRate.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioDataRate.setDescription('Specifies the transmit rate of radio. Here is the available value list. 11a/11g - auto, 1Mb, 2Mb, 5.5Mb, 11Mb, 6Mb, 9Mb, 12Mb, 18Mb, 24Mb, 36Mb, 48Mb, 54Mb. 11ng/11na - auto, 1Mb, 2Mb, 5.5Mb, 11Mb, 6Mb, 9Mb, 12Mb, 18Mb, 24Mb, 36Mb, 48Mb, 54Mb, 6.5Mb, 13Mb, 19.5Mb, 26Mb, 39Mb, 52Mb, 58.5Mb, 65Mb, 78Mb, 104Mb, 117Mb, 130Mb, 13.5Mb, 27.5Mb, 40.5Mb, 81.5Mb, 108Mb, 121.5Mb, 135Mb, 27Mb, 81Mb, 162Mb, 162MB, 216Mb, 243Mb, 270Mb.')
ruckusRadioTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("full", 0), ("half", 1), ("quarter", 2), ("eighth", 3), ("minimum", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusRadioTxPower.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioTxPower.setDescription('Specifies the transmit power of radio')
ruckusRadioProtectionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("ctsOnly", 1), ("ctsRts", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusRadioProtectionMode.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioProtectionMode.setDescription('Enabled when 11g and 11b clients exist on the same network. none: Do not use any protection ctsOnly: AP will send a CTS frame prior to sending 11g frames. The CTS frame will silence 11b clients rtsCts: Require RTS to be sent by sender of 11g frame and responder to send CTS prior to any 11g frames being sent.')
ruckusRadioStatsTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3), )
if mibBuilder.loadTexts: ruckusRadioStatsTable.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsTable.setDescription('Radios statistics table')
ruckusRadioStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ruckusRadioStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsEntry.setDescription('Specifies radio statistics entry.')
ruckusRadioStatsMaxSta = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsMaxSta.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsMaxSta.setDescription('Num of max stations allowed.')
ruckusRadioStatsNumSta = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsNumSta.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsNumSta.setDescription('Num of associated stations.')
ruckusRadioStatsNumAuthSta = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsNumAuthSta.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsNumAuthSta.setDescription('Num of authenticated stations.')
ruckusRadioStatsNumAuthReq = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsNumAuthReq.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsNumAuthReq.setDescription('Number of authentication requests.')
ruckusRadioStatsNumAuthResp = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsNumAuthResp.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsNumAuthResp.setDescription('Number of authentication responses.')
ruckusRadioStatsNumAuthSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsNumAuthSuccess.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsNumAuthSuccess.setDescription('Number of successful authentications.')
ruckusRadioStatsNumAuthFail = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsNumAuthFail.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsNumAuthFail.setDescription('Number of authentication failures.')
ruckusRadioStatsNumAssocReq = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsNumAssocReq.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsNumAssocReq.setDescription('Number of association requests.')
ruckusRadioStatsNumAssocResp = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsNumAssocResp.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsNumAssocResp.setDescription('Number of association responses.')
ruckusRadioStatsNumAssocSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsNumAssocSuccess.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsNumAssocSuccess.setDescription('Number of successful associations.')
ruckusRadioStatsNumAssocFail = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsNumAssocFail.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsNumAssocFail.setDescription('Number of association failures.')
ruckusRadioStatsAssocFailRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsAssocFailRate.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsAssocFailRate.setDescription('Station association fail rate. ruckusRadioStatsNumAssocFail/ruckusRadioStatsNumAssocReq')
ruckusRadioStatsAuthFailRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsAuthFailRate.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsAuthFailRate.setDescription('Station authentication fail rate. ruckusRadioStatsNumAuthFail/ruckusRadioStatsNumAuthReq')
ruckusRadioStatsAssocSuccessRate = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsAssocSuccessRate.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsAssocSuccessRate.setDescription('Station association success rate. ruckusRadioStatsNumAssocSuccess/ruckusRadioStatsNumAssocReq')
ruckusRadioStatsResourceUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsResourceUtil.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsResourceUtil.setDescription('Wireless resource utilization rate. ruckusRadioStatsNumSta/ruckusRadioStatsMaxSta')
ruckusRadioStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsRxBytes.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsRxBytes.setDescription('Count of received bytes.')
ruckusRadioStatsRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsRxFrames.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsRxFrames.setDescription('Count of received frames.')
ruckusRadioStatsRxWEPFail = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsRxWEPFail.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsRxWEPFail.setDescription('Count of received failured WEP frames.')
ruckusRadioStatsRxDecryptCRCError = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsRxDecryptCRCError.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsRxDecryptCRCError.setDescription('Count of received frames with decrypted CRC error.')
ruckusRadioStatsRxMICError = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsRxMICError.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsRxMICError.setDescription('Count of received frames with MIC error.')
ruckusRadioStatsRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsRxErrors.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsRxErrors.setDescription('Count of received error frames.')
ruckusRadioStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsTxBytes.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsTxBytes.setDescription('Count of transmitted bytes.')
ruckusRadioStatsTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 12, 1, 1, 1, 3, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusRadioStatsTxFrames.setStatus('current')
if mibBuilder.loadTexts: ruckusRadioStatsTxFrames.setDescription('Count of transmitted frames.')
mibBuilder.exportSymbols("RUCKUS-RADIO-MIB", ruckusRadioStatsNumAuthReq=ruckusRadioStatsNumAuthReq, ruckusRadioStatsNumAssocSuccess=ruckusRadioStatsNumAssocSuccess, ruckusRadioStatsRxDecryptCRCError=ruckusRadioStatsRxDecryptCRCError, ruckusRadioObjects=ruckusRadioObjects, ruckusRadioStatsRxMICError=ruckusRadioStatsRxMICError, PYSNMP_MODULE_ID=ruckusRadioMIB, ruckusRadioStatsNumAssocFail=ruckusRadioStatsNumAssocFail, ruckusRadioStatsTxFrames=ruckusRadioStatsTxFrames, ruckusRadioNumber=ruckusRadioNumber, ruckusRadioInfo=ruckusRadioInfo, ruckusRadioTable=ruckusRadioTable, ruckusRadioStatsResourceUtil=ruckusRadioStatsResourceUtil, ruckusRadioStatsNumAssocReq=ruckusRadioStatsNumAssocReq, ruckusRadioStatsMaxSta=ruckusRadioStatsMaxSta, ruckusRadioStatsAssocSuccessRate=ruckusRadioStatsAssocSuccessRate, ruckusRadioBSSType=ruckusRadioBSSType, ruckusRadioStatsNumSta=ruckusRadioStatsNumSta, ruckusRadioStatsRxBytes=ruckusRadioStatsRxBytes, ruckusRadioStatsNumAuthSta=ruckusRadioStatsNumAuthSta, ruckusRadioChannel=ruckusRadioChannel, ruckusRadioProtectionMode=ruckusRadioProtectionMode, ruckusRadioStatsTxBytes=ruckusRadioStatsTxBytes, ruckusRadioStatsEntry=ruckusRadioStatsEntry, ruckusRadioMode=ruckusRadioMode, ruckusRadioStatsAuthFailRate=ruckusRadioStatsAuthFailRate, ruckusRadioStatsNumAuthSuccess=ruckusRadioStatsNumAuthSuccess, ruckusRadioStatsRxErrors=ruckusRadioStatsRxErrors, ruckusRadioMIB=ruckusRadioMIB, ruckusRadioTxPower=ruckusRadioTxPower, ruckusRadioStatsRxFrames=ruckusRadioStatsRxFrames, ruckusRadioStatsNumAuthFail=ruckusRadioStatsNumAuthFail, ruckusRadioStatsTable=ruckusRadioStatsTable, ruckusRadioEntry=ruckusRadioEntry, ruckusRadioStatsAssocFailRate=ruckusRadioStatsAssocFailRate, ruckusRadioStatsRxWEPFail=ruckusRadioStatsRxWEPFail, ruckusRadioStatsNumAuthResp=ruckusRadioStatsNumAuthResp, ruckusRadioCountry=ruckusRadioCountry, ruckusRadioDataRate=ruckusRadioDataRate, ruckusRadioStatsNumAssocResp=ruckusRadioStatsNumAssocResp)
