#
# PySNMP MIB module EXTREME-AUTOPROVISION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-AUTOPROVISION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, Gauge32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
extremeAutoProvision = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 40))
extremeAutoProvision.setRevisions(('2010-06-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: extremeAutoProvision.setRevisionsDescriptions(('Initial Revision',))
if mibBuilder.loadTexts: extremeAutoProvision.setLastUpdated('201006040000Z')
if mibBuilder.loadTexts: extremeAutoProvision.setOrganization('Extreme Networks, Inc.')
if mibBuilder.loadTexts: extremeAutoProvision.setContactInfo('www.extremenetworks.com')
if mibBuilder.loadTexts: extremeAutoProvision.setDescription('Extreme Auto Provision feature MIB')
extremeAutoProvisionGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 40, 1))
extremeAutoProvisionNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 40, 2))
extremeAutoProvisionNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 40, 3))
extremeAutoProvisionTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 40, 3, 0))
extremeAutoProvisionConfig = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 40, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeAutoProvisionConfig.setStatus('current')
if mibBuilder.loadTexts: extremeAutoProvisionConfig.setDescription('Auto Provision configuration on the switch (enabled/disabled).')
extremeAutoProvisionStatus = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 40, 3, 0, 1)).setObjects(("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionResult"), ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionIpAddress"), ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionGateway"), ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionTFTPServer"), ("EXTREME-AUTOPROVISION-MIB", "extremeAutoProvisionConfigFileName"))
if mibBuilder.loadTexts: extremeAutoProvisionStatus.setStatus('current')
if mibBuilder.loadTexts: extremeAutoProvisionStatus.setDescription('This trap will reports the auto provision result (success/failed). It contains the attributes it got from the DHCP server.')
extremeAutoProvisionResult = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("invalidConfigFileExtension", 1), ("tftpUnReachable", 2), ("fileNotExist", 3), ("success", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeAutoProvisionResult.setStatus('current')
if mibBuilder.loadTexts: extremeAutoProvisionResult.setDescription('Result of the Auto provision')
extremeAutoProvisionIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 2), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeAutoProvisionIpAddress.setStatus('current')
if mibBuilder.loadTexts: extremeAutoProvisionIpAddress.setDescription('The IP Address received from the DHCP server for this interface.')
extremeAutoProvisionGateway = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 3), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeAutoProvisionGateway.setStatus('current')
if mibBuilder.loadTexts: extremeAutoProvisionGateway.setDescription('The Gateway Address received from the DHCP server for this interface.')
extremeAutoProvisionTFTPServer = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 4), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeAutoProvisionTFTPServer.setStatus('current')
if mibBuilder.loadTexts: extremeAutoProvisionTFTPServer.setDescription('The IP Address of the TFTP Server got from the DHCP Server.')
extremeAutoProvisionConfigFileName = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 40, 2, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeAutoProvisionConfigFileName.setStatus('current')
if mibBuilder.loadTexts: extremeAutoProvisionConfigFileName.setDescription('The Configuration file name got from the DHCP server which the Auto provision enabled switch will download from the TFTP Server and apply the same. It can be with cfg or xsf extension.')
mibBuilder.exportSymbols("EXTREME-AUTOPROVISION-MIB", extremeAutoProvisionGeneral=extremeAutoProvisionGeneral, extremeAutoProvisionNotification=extremeAutoProvisionNotification, extremeAutoProvisionTrapPrefix=extremeAutoProvisionTrapPrefix, extremeAutoProvisionGateway=extremeAutoProvisionGateway, extremeAutoProvisionConfig=extremeAutoProvisionConfig, extremeAutoProvision=extremeAutoProvision, extremeAutoProvisionConfigFileName=extremeAutoProvisionConfigFileName, PYSNMP_MODULE_ID=extremeAutoProvision, extremeAutoProvisionStatus=extremeAutoProvisionStatus, extremeAutoProvisionNotificationObjects=extremeAutoProvisionNotificationObjects, extremeAutoProvisionIpAddress=extremeAutoProvisionIpAddress, extremeAutoProvisionResult=extremeAutoProvisionResult, extremeAutoProvisionTFTPServer=extremeAutoProvisionTFTPServer)
