#
# PySNMP MIB module MGMT-SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MGMT-SECURITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
switch, quanta = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch", "quanta")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, Counter32, IpAddress, Integer32, TimeTicks, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, ModuleIdentity, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Counter32", "IpAddress", "Integer32", "TimeTicks", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "ModuleIdentity", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
mgmtSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 11))
if mibBuilder.loadTexts: mgmtSecurity.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: mgmtSecurity.setOrganization('Quanta Computer Inc.')
agentSSLConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1))
agentSSLAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLAdminMode.setStatus('current')
agentSSLSecurePort = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLSecurePort.setStatus('current')
agentSSLProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssl30", 1), ("tls10", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLProtocolLevel.setStatus('current')
agentSSLMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLMaxSessions.setStatus('current')
agentSSLHardTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 168))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLHardTimeout.setStatus('current')
agentSSLSoftTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLSoftTimeout.setStatus('current')
agentSSLCertificatePresent = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSLCertificatePresent.setStatus('current')
agentSSLCertificateControl = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("generate", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSLCertificateControl.setStatus('current')
agentSSLCertificateGenerationStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSLCertificateGenerationStatus.setStatus('current')
agentSSHConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2))
agentSSHAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHAdminMode.setStatus('current')
agentSSHProtocolLevel = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ssh10", 1), ("ssh20", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHProtocolLevel.setStatus('current')
agentSSHSessionsCount = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSHSessionsCount.setStatus('current')
agentSSHMaxSessionsCount = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHMaxSessionsCount.setStatus('current')
agentSSHSessionTimeout = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHSessionTimeout.setStatus('current')
agentSSHKeysPresent = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dsa", 1), ("rsa", 2), ("both", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSHKeysPresent.setStatus('current')
agentSSHKeyGenerationStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dsa", 1), ("rsa", 2), ("both", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentSSHKeyGenerationStatus.setStatus('current')
agentSSHRSAKeyControl = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("generate", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHRSAKeyControl.setStatus('current')
agentSSHDSAKeyControl = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 11, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("generate", 2), ("delete", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentSSHDSAKeyControl.setStatus('current')
mibBuilder.exportSymbols("MGMT-SECURITY-MIB", agentSSLCertificateGenerationStatus=agentSSLCertificateGenerationStatus, agentSSLSecurePort=agentSSLSecurePort, agentSSHProtocolLevel=agentSSHProtocolLevel, agentSSHKeysPresent=agentSSHKeysPresent, mgmtSecurity=mgmtSecurity, agentSSLConfigGroup=agentSSLConfigGroup, agentSSHAdminMode=agentSSHAdminMode, agentSSLAdminMode=agentSSLAdminMode, PYSNMP_MODULE_ID=mgmtSecurity, agentSSLProtocolLevel=agentSSLProtocolLevel, agentSSHDSAKeyControl=agentSSHDSAKeyControl, agentSSHMaxSessionsCount=agentSSHMaxSessionsCount, agentSSLCertificateControl=agentSSLCertificateControl, agentSSHConfigGroup=agentSSHConfigGroup, agentSSLHardTimeout=agentSSLHardTimeout, agentSSLSoftTimeout=agentSSLSoftTimeout, agentSSLCertificatePresent=agentSSLCertificatePresent, agentSSHRSAKeyControl=agentSSHRSAKeyControl, agentSSHSessionsCount=agentSSHSessionsCount, agentSSHSessionTimeout=agentSSHSessionTimeout, agentSSLMaxSessions=agentSSLMaxSessions, agentSSHKeyGenerationStatus=agentSSHKeyGenerationStatus)
