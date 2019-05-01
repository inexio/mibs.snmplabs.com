#
# PySNMP MIB module AISLCASYNC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AISLCASYNC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:16:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, NotificationType, Gauge32, ObjectIdentity, MibIdentifier, Bits, IpAddress, ModuleIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "NotificationType", "Gauge32", "ObjectIdentity", "MibIdentifier", "Bits", "IpAddress", "ModuleIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Integer32", "Unsigned32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSLCAsync = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 23))
if mibBuilder.loadTexts: aiSLCAsync.setLastUpdated('9909151700Z')
if mibBuilder.loadTexts: aiSLCAsync.setOrganization('Applied Innovation Inc.')
if mibBuilder.loadTexts: aiSLCAsync.setContactInfo('Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 Email: snmp@aiinet.com')
if mibBuilder.loadTexts: aiSLCAsync.setDescription('MIB module for SLCs with asynchronous links.')
aiSLCAsyncTable = MibTable((1, 3, 6, 1, 4, 1, 539, 23, 1), )
if mibBuilder.loadTexts: aiSLCAsyncTable.setStatus('current')
if mibBuilder.loadTexts: aiSLCAsyncTable.setDescription('Table of asynchronous link information indexed by link number. Includes link appplication and direct connect alias.')
aiSLCAsyncEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 23, 1, 1), ).setIndexNames((0, "AISLCASYNC-MIB", "aislcasyLinkNumber"))
if mibBuilder.loadTexts: aiSLCAsyncEntry.setStatus('current')
if mibBuilder.loadTexts: aiSLCAsyncEntry.setDescription('Entry of aiSLCAsyncTable.')
aislcasyLinkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcasyLinkNumber.setStatus('current')
if mibBuilder.loadTexts: aislcasyLinkNumber.setDescription('Link number to which this table row applies.')
aislcasyApplication = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("login", 1), ("destination", 2), ("directConnect", 3), ("callMenu", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcasyApplication.setStatus('current')
if mibBuilder.loadTexts: aislcasyApplication.setDescription('Application configured for the this link. login(1): Link provides a login prompt. destination(2): Link is only a destination and cannot be used to place calls. directConnect(3): Link connects directly to the destination stored in aislcasyDirectConnectAlias. callMenu(4): Link provides a menu of destinations to which calls can be placed.')
aislcasyDirectConnectAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcasyDirectConnectAlias.setStatus('current')
if mibBuilder.loadTexts: aislcasyDirectConnectAlias.setDescription('Alias used when aislcasyApplication is directConnect(3). Maximum length is 255 characters.')
aislcasyXonInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 120))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcasyXonInterval.setStatus('current')
if mibBuilder.loadTexts: aislcasyXonInterval.setDescription('Time between sending successive XON characters. Maximum is 120 seconds. Zero disables sending periodic XONs.')
aislcasyCallState = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcasyCallState.setStatus('current')
if mibBuilder.loadTexts: aislcasyCallState.setDescription('Read only string describing the current link call state.')
aislcasyMinimizeLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcasyMinimizeLatency.setStatus('current')
if mibBuilder.loadTexts: aislcasyMinimizeLatency.setDescription('Minimizes buffer latency.')
aiSLCAsyncConnOptTable = MibTable((1, 3, 6, 1, 4, 1, 539, 23, 2), )
if mibBuilder.loadTexts: aiSLCAsyncConnOptTable.setStatus('current')
if mibBuilder.loadTexts: aiSLCAsyncConnOptTable.setDescription('Table of asynchronous link connect options indexed by link number. Includes settings for when and how to establish connections.')
aiSLCAsyncConnOptEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 23, 2, 1), ).setIndexNames((0, "AISLCASYNC-MIB", "aislcacoLinkNumber"))
if mibBuilder.loadTexts: aiSLCAsyncConnOptEntry.setStatus('current')
if mibBuilder.loadTexts: aiSLCAsyncConnOptEntry.setDescription('Entry of aiSLCAsyncConnOptTable.')
aislcacoLinkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcacoLinkNumber.setStatus('current')
if mibBuilder.loadTexts: aislcacoLinkNumber.setDescription('Link number to which this table row applies.')
aislcacoOnActiveDSR = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcacoOnActiveDSR.setStatus('current')
if mibBuilder.loadTexts: aislcacoOnActiveDSR.setDescription('Consider link active when DSR is active.')
aislcacoOnActiveDCD = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcacoOnActiveDCD.setStatus('current')
if mibBuilder.loadTexts: aislcacoOnActiveDCD.setDescription('Consider link active when DCD is active.')
aislcacoOnIncomingChar = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcacoOnIncomingChar.setStatus('current')
if mibBuilder.loadTexts: aislcacoOnIncomingChar.setDescription('Consider link active when characters are received.')
aislcacoDirectConnect = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcacoDirectConnect.setStatus('current')
if mibBuilder.loadTexts: aislcacoDirectConnect.setDescription('Connect to destination specified in aislcasyDirectConnectAlias as soon as the link is enabled. This overrides other connection options.')
aislcacoRetryTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcacoRetryTimer.setStatus('current')
if mibBuilder.loadTexts: aislcacoRetryTimer.setDescription('Wait interval after unsuccessful call. Maximum is 32767 seconds. Zero disables retry.')
aislcacoConnectString = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcacoConnectString.setStatus('current')
if mibBuilder.loadTexts: aislcacoConnectString.setDescription('String to send immediately after a call is established. Maximum length is 80 characters.')
aiSLCAsyncDiscOptTable = MibTable((1, 3, 6, 1, 4, 1, 539, 23, 3), )
if mibBuilder.loadTexts: aiSLCAsyncDiscOptTable.setStatus('current')
if mibBuilder.loadTexts: aiSLCAsyncDiscOptTable.setDescription('Table of asynchronous link disconnect options indexed by link number. Includes settings for when and how to close connections.')
aiSLCAsyncDiscOptEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 23, 3, 1), ).setIndexNames((0, "AISLCASYNC-MIB", "aislcadoLinkNumber"))
if mibBuilder.loadTexts: aiSLCAsyncDiscOptEntry.setStatus('current')
if mibBuilder.loadTexts: aiSLCAsyncDiscOptEntry.setDescription('Entry of aiSLCAsyncDiscOptTable.')
aislcadoLinkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcadoLinkNumber.setStatus('current')
if mibBuilder.loadTexts: aislcadoLinkNumber.setDescription('Link number to which this table row applies.')
aislcadoOnLostDSR = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcadoOnLostDSR.setStatus('current')
if mibBuilder.loadTexts: aislcadoOnLostDSR.setDescription('Disconnect call when DSR is lost.')
aislcadoOnLostDCD = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcadoOnLostDCD.setStatus('current')
if mibBuilder.loadTexts: aislcadoOnLostDCD.setDescription('Disconnect call when DCD is lost.')
aislcadoOnBreak = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcadoOnBreak.setStatus('current')
if mibBuilder.loadTexts: aislcadoOnBreak.setDescription('Disconnect call when a break character is received.')
aislcadoInactivityTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcadoInactivityTimer.setStatus('current')
if mibBuilder.loadTexts: aislcadoInactivityTimer.setDescription('Interval of inactivity after which a call is disconnected. Maximum is 32767 seconds. Zero disables disconnect-on-inactivty.')
aislcadoDisconnectString = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcadoDisconnectString.setStatus('current')
if mibBuilder.loadTexts: aislcadoDisconnectString.setDescription('String to send immediately before a call is disconnected. Maximum length is 80 characters.')
aislcadoInactivityReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 3, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcadoInactivityReceive.setStatus('current')
if mibBuilder.loadTexts: aislcadoInactivityReceive.setDescription('Inactivity Timer enabled when link receives calls.')
aiSLCAsyncModemOptTable = MibTable((1, 3, 6, 1, 4, 1, 539, 23, 4), )
if mibBuilder.loadTexts: aiSLCAsyncModemOptTable.setStatus('current')
if mibBuilder.loadTexts: aiSLCAsyncModemOptTable.setDescription('Table of asynchronous link modem options indexed by link number. Includes settings for modem strings, dialing timeout, retry limit, and signal lead options.')
aiSLCAsyncModemOptEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 23, 4, 1), ).setIndexNames((0, "AISLCASYNC-MIB", "aislcmdmLinkNumber"))
if mibBuilder.loadTexts: aiSLCAsyncModemOptEntry.setStatus('current')
if mibBuilder.loadTexts: aiSLCAsyncModemOptEntry.setDescription('Entry of aiSLCAsyncModemOptTable.')
aislcmdmLinkNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcmdmLinkNumber.setStatus('current')
if mibBuilder.loadTexts: aislcmdmLinkNumber.setDescription('Link number to which this table row applies.')
aislcmdmInitString = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcmdmInitString.setStatus('current')
if mibBuilder.loadTexts: aislcmdmInitString.setDescription('String to send when a link is enabled or restarted, possibly to place a modem in auto-answer mode, to cause a modem to dial a remote location, or to prepare a modem in some other way. Maximum length is 80 characters.')
aislcmdmTermString = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcmdmTermString.setStatus('current')
if mibBuilder.loadTexts: aislcmdmTermString.setDescription('String to send immediately after the disconnect string, before a call is disconnected, possibly for the bennefit of an attached modem. Maximum length is 80 characters.')
aislcmdmTimeToConnect = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcmdmTimeToConnect.setStatus('current')
if mibBuilder.loadTexts: aislcmdmTimeToConnect.setDescription('Number of seconds to wait for modem to connect after dialing. Maximum is 300 seconds. Minimum is 5 seconds')
aislcmdmMaxDialAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcmdmMaxDialAttempts.setStatus('current')
if mibBuilder.loadTexts: aislcmdmMaxDialAttempts.setDescription('Maximum number of times to dial when placing an outgoing call. Maximum is 100 attempts. Zero retrys dialing forever.')
aislcmdmDtrConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcmdmDtrConnState.setStatus('current')
if mibBuilder.loadTexts: aislcmdmDtrConnState.setDescription('State of DTR when connected or connecting. on(1): DTR is on when link is connected or connecting. off(2): DTR is off when link is connected or connecting.')
aislcmdmDtrDconnState = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("toggle", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcmdmDtrDconnState.setStatus('current')
if mibBuilder.loadTexts: aislcmdmDtrDconnState.setDescription('State of DTR when disconnected. on(1): DTR is on when link is disconnected. off(2): DTR is off when link is disconnected. toggle(3): DTR toggles on-to-off when link disconnects.')
aislcmdmRtsConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("followsDSR", 3), ("xmitFlowControl", 4), ("bidirectionalFlowControl", 5), ("followsData", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcmdmRtsConnState.setStatus('current')
if mibBuilder.loadTexts: aislcmdmRtsConnState.setDescription('State of DTR when connected or connecting. on(1), RTS is on when link is connected or connecting. off(2), RTS is off when link is connected or connecting. followsDSR(3), RTS follows the state of DSR when link is connected or connecting. xmitFlowControl(4), RTS is on when the DTE has data to send, and DTE sends only when DCE asserts CTS on. bidirectionalFlowControl(5) RTS is on when DTE is ready to accept data from DCE, and DTE sends only when DCE asserts CTS on followsData(6), RTS is asserted only when data is transmitted.')
aislcmdmRtsDconnState = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 23, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("toggle", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aislcmdmRtsDconnState.setStatus('current')
if mibBuilder.loadTexts: aislcmdmRtsDconnState.setDescription('State of RTS when disconnected. on(1): RTS is on when link is disconnected. off(2): RTS is off when link is disconnected. toggle(3): DTR toggles on-to-off when link disconnects.')
mibBuilder.exportSymbols("AISLCASYNC-MIB", aiSLCAsyncConnOptEntry=aiSLCAsyncConnOptEntry, aislcadoInactivityTimer=aislcadoInactivityTimer, aiSLCAsyncEntry=aiSLCAsyncEntry, aiSLCAsyncDiscOptEntry=aiSLCAsyncDiscOptEntry, aislcmdmRtsConnState=aislcmdmRtsConnState, aislcmdmRtsDconnState=aislcmdmRtsDconnState, aislcadoDisconnectString=aislcadoDisconnectString, aislcacoDirectConnect=aislcacoDirectConnect, aislcmdmMaxDialAttempts=aislcmdmMaxDialAttempts, aislcacoRetryTimer=aislcacoRetryTimer, aislcasyCallState=aislcasyCallState, aislcasyApplication=aislcasyApplication, aislcmdmLinkNumber=aislcmdmLinkNumber, aislcadoOnLostDCD=aislcadoOnLostDCD, aiSLCAsync=aiSLCAsync, aislcasyXonInterval=aislcasyXonInterval, aiSLCAsyncConnOptTable=aiSLCAsyncConnOptTable, PositiveInteger=PositiveInteger, aislcadoLinkNumber=aislcadoLinkNumber, aiSLCAsyncModemOptTable=aiSLCAsyncModemOptTable, aislcmdmTimeToConnect=aislcmdmTimeToConnect, aislcmdmDtrDconnState=aislcmdmDtrDconnState, aislcadoOnLostDSR=aislcadoOnLostDSR, aislcacoOnActiveDCD=aislcacoOnActiveDCD, aiSLCAsyncDiscOptTable=aiSLCAsyncDiscOptTable, aislcacoOnActiveDSR=aislcacoOnActiveDSR, aislcasyDirectConnectAlias=aislcasyDirectConnectAlias, aislcacoLinkNumber=aislcacoLinkNumber, aiSLCAsyncTable=aiSLCAsyncTable, PYSNMP_MODULE_ID=aiSLCAsync, aislcmdmTermString=aislcmdmTermString, aislcadoInactivityReceive=aislcadoInactivityReceive, aislcasyMinimizeLatency=aislcasyMinimizeLatency, aislcacoOnIncomingChar=aislcacoOnIncomingChar, aislcacoConnectString=aislcacoConnectString, aislcmdmDtrConnState=aislcmdmDtrConnState, aii=aii, aislcmdmInitString=aislcmdmInitString, aiSLCAsyncModemOptEntry=aiSLCAsyncModemOptEntry, aislcasyLinkNumber=aislcasyLinkNumber, aislcadoOnBreak=aislcadoOnBreak)
