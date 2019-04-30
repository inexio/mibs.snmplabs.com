#
# PySNMP MIB module NOKIA-AZC-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-AZC-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, Counter64, Counter32, enterprises, NotificationType, Integer32, IpAddress, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "Counter64", "Counter32", "enterprises", "NotificationType", "Integer32", "IpAddress", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
nokia = MibIdentifier((1, 3, 6, 1, 4, 1, 94))
nokiaProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1))
azcProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32))
azcSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32, 2))
azcStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1))
azcVersion = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcVersion.setStatus('mandatory')
azcRelease = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcRelease.setStatus('mandatory')
azcStarted = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcStarted.setStatus('mandatory')
azcLoginsSuccess = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsSuccess.setStatus('mandatory')
azcLoginsAuthFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsAuthFailures.setStatus('mandatory')
azcLoginsACLFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsACLFailures.setStatus('mandatory')
azcLoginsDuplFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsDuplFailures.setStatus('mandatory')
azcLoginsSpaceFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsSpaceFailures.setStatus('mandatory')
azcLoginsRADIUSFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsRADIUSFailures.setStatus('mandatory')
azcLoginsRADIUSACLFailures = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginsRADIUSACLFailures.setStatus('mandatory')
azcAutologoffsRADIUS = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsRADIUS.setStatus('mandatory')
azcAutologoffsPing = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsPing.setStatus('mandatory')
azcAutologoffsMAC = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsMAC.setStatus('mandatory')
azcAutologoffsACL = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsACL.setStatus('mandatory')
azcAutologoffsQuota = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsQuota.setStatus('mandatory')
azcAutologoffsMaxTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsMaxTime.setStatus('mandatory')
azcAutologoffsIdletimer = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcAutologoffsIdletimer.setStatus('mandatory')
azcPktsIntIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsIntIn.setStatus('mandatory')
azcPktsIntOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsIntOut.setStatus('mandatory')
azcBytesIntIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesIntIn.setStatus('mandatory')
azcBytesIntOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesIntOut.setStatus('mandatory')
azcPktsExtIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsExtIn.setStatus('mandatory')
azcPktsExtOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsExtOut.setStatus('mandatory')
azcBytesExtIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesExtIn.setStatus('mandatory')
azcBytesExtOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesExtOut.setStatus('mandatory')
azcPktsNattedIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsNattedIn.setStatus('mandatory')
azcPktsNattedOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsNattedOut.setStatus('mandatory')
azcBytesNattedIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesNattedIn.setStatus('mandatory')
azcBytesNattedOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesNattedOut.setStatus('mandatory')
azcPktsNattedErrIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsNattedErrIn.setStatus('mandatory')
azcPktsNattedErrOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsNattedErrOut.setStatus('mandatory')
azcBytesNattedErrIn = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesNattedErrIn.setStatus('mandatory')
azcBytesNattedErrOut = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesNattedErrOut.setStatus('mandatory')
azcPktsRejInt = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsRejInt.setStatus('mandatory')
azcPktsRejExt = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPktsRejExt.setStatus('mandatory')
azcBytesRejInt = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesRejInt.setStatus('mandatory')
azcBytesRejExt = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBytesRejExt.setStatus('mandatory')
azcACLSelectErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLSelectErr.setStatus('mandatory')
azcACLSendmsgErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLSendmsgErr.setStatus('mandatory')
azcACLRevmsgErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgErr.setStatus('mandatory')
azcACLRevmsgOverflow = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgOverflow.setStatus('mandatory')
azcACLSendmsgLocErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLSendmsgLocErr.setStatus('mandatory')
azcACLRevmsgLocErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 43), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgLocErr.setStatus('mandatory')
azcACLRevmsgLocOverflow = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 44), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgLocOverflow.setStatus('mandatory')
azcACLRevmsgCtlErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 45), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgCtlErr.setStatus('mandatory')
azcACLRevmsgCtlOverflow = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 46), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLRevmsgCtlOverflow.setStatus('mandatory')
azcACLMemAllocs = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 47), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLMemAllocs.setStatus('mandatory')
azcACLMemAllocErr = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 48), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcACLMemAllocErr.setStatus('mandatory')
azcActivationKey = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 49), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcActivationKey.setStatus('mandatory')
azcHostID = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 50), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcHostID.setStatus('mandatory')
azcIntIf = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 51), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcIntIf.setStatus('mandatory')
azcExtIf = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 52), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcExtIf.setStatus('mandatory')
azcMaxTimeout = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 53), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMaxTimeout.setStatus('mandatory')
azcMaxIdleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 54), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMaxIdleTimeout.setStatus('mandatory')
azcPingPeriod = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 55), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcPingPeriod.setStatus('mandatory')
azcLoginURL = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 56), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginURL.setStatus('mandatory')
azcIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 57), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcIPAddress.setStatus('mandatory')
azcExtIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 58), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcExtIPAddress.setStatus('mandatory')
azcDNSIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 59), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcDNSIPAddress.setStatus('mandatory')
azcDHCPIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 60), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcDHCPIPAddress.setStatus('mandatory')
azcProxyHost = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 61), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcProxyHost.setStatus('mandatory')
azcProxyPorts = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 62), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcProxyPorts.setStatus('mandatory')
azcMailRelayHost = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 63), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMailRelayHost.setStatus('mandatory')
azcRADIUSAlivePeriod = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 64), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcRADIUSAlivePeriod.setStatus('mandatory')
azcRADIUSAliveTrigger = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 65), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcRADIUSAliveTrigger.setStatus('mandatory')
azcWhitelist = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 66), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcWhitelist.setStatus('mandatory')
azcBlackList = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 67), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcBlackList.setStatus('mandatory')
azcDemoAccounts = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 68), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcDemoAccounts.setStatus('mandatory')
azcUDPFilter = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 69), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcUDPFilter.setStatus('mandatory')
azcCutTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 70), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcCutTime.setStatus('mandatory')
azcCutSafetyTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 71), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcCutSafetyTime.setStatus('mandatory')
azcRADIUSActivated = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 72), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcRADIUSActivated.setStatus('mandatory')
azcMACCheckMode = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 73), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMACCheckMode.setStatus('mandatory')
azcNATState = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 74), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcNATState.setStatus('mandatory')
azcDHCPState = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 75), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcDHCPState.setStatus('mandatory')
azcSSLState = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 76), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcSSLState.setStatus('mandatory')
azcSNMPTrapState = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 77), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcSNMPTrapState.setStatus('mandatory')
azcMACAuthState = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 78), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMACAuthState.setStatus('mandatory')
azcMACRealm = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 79), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMACRealm.setStatus('mandatory')
azcMACPassword = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 80), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcMACPassword.setStatus('mandatory')
azcNATDArgs = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 81), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcNATDArgs.setStatus('mandatory')
azcSyslogFacility = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 82), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcSyslogFacility.setStatus('mandatory')
azcSyslogLevel = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 83), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 4, 6))).clone(namedValues=NamedValues(("nothing", 0), ("onlyErrors", 1), ("alsoWarnings", 4), ("alsoInfo", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcSyslogLevel.setStatus('mandatory')
azcQOSClass1 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 84), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcQOSClass1.setStatus('mandatory')
azcQOSClass2 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 85), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcQOSClass2.setStatus('mandatory')
azcQOSClass3 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 86), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcQOSClass3.setStatus('mandatory')
azcQOSClassDefault = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 87), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcQOSClassDefault.setStatus('mandatory')
azcLocation = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 88), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLocation.setStatus('mandatory')
azcUptime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 89), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcUptime.setStatus('mandatory')
azcTrialTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 90), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcTrialTime.setStatus('mandatory')
azcTrialLockime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 91), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcTrialLockime.setStatus('mandatory')
azcNokiaAuthMode = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 92), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcNokiaAuthMode.setStatus('mandatory')
azcActiveLogins = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 93), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcActiveLogins.setStatus('mandatory')
azcZoneName = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 94), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcZoneName.setStatus('mandatory')
azcLoginTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 32, 2, 1, 95), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: azcLoginTime.setStatus('mandatory')
mibBuilder.exportSymbols("NOKIA-AZC-SYSTEM-MIB", azcACLMemAllocErr=azcACLMemAllocErr, azcBytesIntIn=azcBytesIntIn, azcLoginsRADIUSFailures=azcLoginsRADIUSFailures, azcDNSIPAddress=azcDNSIPAddress, azcLoginsSpaceFailures=azcLoginsSpaceFailures, azcLoginsDuplFailures=azcLoginsDuplFailures, azcBlackList=azcBlackList, azcPktsIntOut=azcPktsIntOut, azcActiveLogins=azcActiveLogins, azcRADIUSAliveTrigger=azcRADIUSAliveTrigger, azcACLRevmsgOverflow=azcACLRevmsgOverflow, azcLoginsRADIUSACLFailures=azcLoginsRADIUSACLFailures, azcAutologoffsIdletimer=azcAutologoffsIdletimer, azcIntIf=azcIntIf, azcAutologoffsQuota=azcAutologoffsQuota, azcPktsRejExt=azcPktsRejExt, azcDHCPIPAddress=azcDHCPIPAddress, azcBytesIntOut=azcBytesIntOut, azcMACCheckMode=azcMACCheckMode, azcCutTime=azcCutTime, azcACLRevmsgCtlErr=azcACLRevmsgCtlErr, azcPingPeriod=azcPingPeriod, azcLocation=azcLocation, azcUDPFilter=azcUDPFilter, azcTrialLockime=azcTrialLockime, azcPktsExtOut=azcPktsExtOut, azcQOSClassDefault=azcQOSClassDefault, azcAutologoffsPing=azcAutologoffsPing, azcZoneName=azcZoneName, azcMACRealm=azcMACRealm, azcLoginTime=azcLoginTime, azcAutologoffsMaxTime=azcAutologoffsMaxTime, azcSyslogFacility=azcSyslogFacility, azcProxyHost=azcProxyHost, azcAutologoffsMAC=azcAutologoffsMAC, azcBytesRejInt=azcBytesRejInt, azcQOSClass3=azcQOSClass3, azcMACPassword=azcMACPassword, azcACLSendmsgErr=azcACLSendmsgErr, azcBytesNattedOut=azcBytesNattedOut, azcWhitelist=azcWhitelist, azcSSLState=azcSSLState, azcRelease=azcRelease, azcQOSClass2=azcQOSClass2, nokiaProducts=nokiaProducts, azcMaxIdleTimeout=azcMaxIdleTimeout, azcRADIUSAlivePeriod=azcRADIUSAlivePeriod, azcIPAddress=azcIPAddress, azcBytesNattedErrIn=azcBytesNattedErrIn, azcHostID=azcHostID, azcACLSendmsgLocErr=azcACLSendmsgLocErr, azcBytesExtIn=azcBytesExtIn, azcQOSClass1=azcQOSClass1, azcLoginsSuccess=azcLoginsSuccess, azcActivationKey=azcActivationKey, azcStatusGroup=azcStatusGroup, azcACLSelectErr=azcACLSelectErr, azcACLMemAllocs=azcACLMemAllocs, azcACLRevmsgErr=azcACLRevmsgErr, azcNATState=azcNATState, azcProxyPorts=azcProxyPorts, azcBytesNattedIn=azcBytesNattedIn, azcMaxTimeout=azcMaxTimeout, azcSyslogLevel=azcSyslogLevel, azcTrialTime=azcTrialTime, azcExtIf=azcExtIf, azcDemoAccounts=azcDemoAccounts, azcBytesNattedErrOut=azcBytesNattedErrOut, azcPktsNattedErrOut=azcPktsNattedErrOut, azcSNMPTrapState=azcSNMPTrapState, azcLoginsACLFailures=azcLoginsACLFailures, nokia=nokia, azcDHCPState=azcDHCPState, azcRADIUSActivated=azcRADIUSActivated, azcLoginURL=azcLoginURL, azcACLRevmsgLocOverflow=azcACLRevmsgLocOverflow, azcProducts=azcProducts, azcBytesExtOut=azcBytesExtOut, azcMailRelayHost=azcMailRelayHost, azcACLRevmsgCtlOverflow=azcACLRevmsgCtlOverflow, azcPktsNattedIn=azcPktsNattedIn, azcVersion=azcVersion, azcPktsExtIn=azcPktsExtIn, azcNokiaAuthMode=azcNokiaAuthMode, azcPktsNattedOut=azcPktsNattedOut, azcACLRevmsgLocErr=azcACLRevmsgLocErr, azcExtIPAddress=azcExtIPAddress, azcLoginsAuthFailures=azcLoginsAuthFailures, azcAutologoffsRADIUS=azcAutologoffsRADIUS, azcMACAuthState=azcMACAuthState, azcSystem=azcSystem, azcAutologoffsACL=azcAutologoffsACL, azcStarted=azcStarted, azcPktsIntIn=azcPktsIntIn, azcPktsRejInt=azcPktsRejInt, azcPktsNattedErrIn=azcPktsNattedErrIn, azcBytesRejExt=azcBytesRejExt, azcUptime=azcUptime, azcCutSafetyTime=azcCutSafetyTime, azcNATDArgs=azcNATDArgs)