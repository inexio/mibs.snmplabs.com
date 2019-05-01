#
# PySNMP MIB module RBN-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-ENVMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Bits, Unsigned32, MibIdentifier, ModuleIdentity, Integer32, TimeTicks, ObjectIdentity, IpAddress, iso, Counter64, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32", "TimeTicks", "ObjectIdentity", "IpAddress", "iso", "Counter64", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
rbnEnvMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 4))
if mibBuilder.loadTexts: rbnEnvMonMIB.setLastUpdated('9901272300Z')
if mibBuilder.loadTexts: rbnEnvMonMIB.setOrganization('RedBack Networks, Inc.')
if mibBuilder.loadTexts: rbnEnvMonMIB.setContactInfo(' RedBack Networks, Inc. Postal: 1389 Moffett Park Drive Sunnyvale, CA 94089-1134 USA Phone: +1 408 548 3500 Fax: +1 408 548 3599 E-mail: mib-info@RedBackNetworks.com')
if mibBuilder.loadTexts: rbnEnvMonMIB.setDescription('The MIB used to genericially manage Environmental Monitor functionality on RedBack Networks devices.')
rbnEnvMonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 4, 0))
rbnEnvMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1))
rbnEnvMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2))
rbnFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1), )
if mibBuilder.loadTexts: rbnFanStatusTable.setStatus('current')
if mibBuilder.loadTexts: rbnFanStatusTable.setDescription('This table contains one row per fan test point. Note that there is not necessarily a one-to-one relationship between fan test points and fan assemblies; a single test point may be used to monitor the status of multiple fans.')
rbnFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1), ).setIndexNames((0, "RBN-ENVMON-MIB", "rbnFanIndex"))
if mibBuilder.loadTexts: rbnFanStatusEntry.setStatus('current')
if mibBuilder.loadTexts: rbnFanStatusEntry.setDescription('Information about a particular fan test point')
rbnFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rbnFanIndex.setStatus('current')
if mibBuilder.loadTexts: rbnFanIndex.setDescription('The index of a fan test point.')
rbnFanDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFanDescr.setStatus('current')
if mibBuilder.loadTexts: rbnFanDescr.setDescription('The description of a fan test point. If an instance of this object is associated with a single fan assembly, then the value of this object should be the same as the name by which the assembly is normally referenced. If an instance is associated with multiple fan assemblies, then the value of this object should contain the names of all of the fan assemblies being monitored.')
rbnFanFail = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnFanFail.setStatus('current')
if mibBuilder.loadTexts: rbnFanFail.setDescription('The status of a fan test point. If an instance of this object has the value true, then a fan monitored by the test point has failed. If an instance of this object has the value false, then the fan (or fans) monitored by the test point are operational.')
rbnPowerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2), )
if mibBuilder.loadTexts: rbnPowerStatusTable.setStatus('current')
if mibBuilder.loadTexts: rbnPowerStatusTable.setDescription('This table contains one row per power test point. Note that there is not necessarily a one-to-one relationship between power test points and power supply assemblies; a single test point may be used to monitor the status of multiple power supplies.')
rbnPowerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1), ).setIndexNames((0, "RBN-ENVMON-MIB", "rbnPowerIndex"))
if mibBuilder.loadTexts: rbnPowerStatusEntry.setStatus('current')
if mibBuilder.loadTexts: rbnPowerStatusEntry.setDescription('Information about a particular power test point')
rbnPowerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rbnPowerIndex.setStatus('current')
if mibBuilder.loadTexts: rbnPowerIndex.setDescription('The index of a power test point.')
rbnPowerDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnPowerDescr.setStatus('current')
if mibBuilder.loadTexts: rbnPowerDescr.setDescription('The description of a power supply test point. If an instance of this object is associated with a single power supply assembly, then the value of this object should be the same as the name by which the assembly is normally referenced. If an instance is associated with multiple power supply assemblies, then the value of this object should contain the names of all of the power supply assemblies being monitored.')
rbnPowerFail = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 4, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnPowerFail.setStatus('current')
if mibBuilder.loadTexts: rbnPowerFail.setDescription('The status of a power test point. If an instance of this object has the value true, then a power supply monitored by the test point has failed. If an instance of this object has the value false, then the power supply (or supplies) monitored by the test point are operational.')
rbnFanFailChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 1)).setObjects(("RBN-ENVMON-MIB", "rbnFanFail"))
if mibBuilder.loadTexts: rbnFanFailChange.setStatus('current')
if mibBuilder.loadTexts: rbnFanFailChange.setDescription('A rbnFanFailChange notification signifies that the value of an instance of rbnFanFail has changed.')
rbnPowerFailChange = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 4, 0, 2)).setObjects(("RBN-ENVMON-MIB", "rbnPowerFail"))
if mibBuilder.loadTexts: rbnPowerFailChange.setStatus('current')
if mibBuilder.loadTexts: rbnPowerFailChange.setDescription('A rbnPowerFailChange notification signifies that the value of an instance of rbnPowerFail has changed')
rbnEnvMonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1))
rbnEnvMonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2))
rbnEnvMonMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 1)).setObjects(("RBN-ENVMON-MIB", "rbnFanDescr"), ("RBN-ENVMON-MIB", "rbnFanFail"), ("RBN-ENVMON-MIB", "rbnPowerDescr"), ("RBN-ENVMON-MIB", "rbnPowerFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBObjectGroup = rbnEnvMonMIBObjectGroup.setStatus('current')
if mibBuilder.loadTexts: rbnEnvMonMIBObjectGroup.setDescription('A collection of objects providing environmental monitor information.')
rbnEnvMonMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 1, 2)).setObjects(("RBN-ENVMON-MIB", "rbnFanFailChange"), ("RBN-ENVMON-MIB", "rbnPowerFailChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBNotificationGroup = rbnEnvMonMIBNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: rbnEnvMonMIBNotificationGroup.setDescription('A collection of notifications providing environmental monitor information.')
rbnEnvMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 4, 2, 2, 1)).setObjects(("RBN-ENVMON-MIB", "rbnEnvMonMIBObjectGroup"), ("RBN-ENVMON-MIB", "rbnEnvMonMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnEnvMonMIBCompliance = rbnEnvMonMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnEnvMonMIBCompliance.setDescription('The compliance statement for the EnvMon MIB')
mibBuilder.exportSymbols("RBN-ENVMON-MIB", rbnPowerStatusTable=rbnPowerStatusTable, PYSNMP_MODULE_ID=rbnEnvMonMIB, rbnPowerDescr=rbnPowerDescr, rbnEnvMonMIBCompliances=rbnEnvMonMIBCompliances, rbnEnvMonMIBObjectGroup=rbnEnvMonMIBObjectGroup, rbnEnvMonMIB=rbnEnvMonMIB, rbnFanDescr=rbnFanDescr, rbnEnvMonMIBConformance=rbnEnvMonMIBConformance, rbnEnvMonMIBGroups=rbnEnvMonMIBGroups, rbnFanFail=rbnFanFail, rbnEnvMonMIBNotificationGroup=rbnEnvMonMIBNotificationGroup, rbnEnvMonMIBCompliance=rbnEnvMonMIBCompliance, rbnPowerFail=rbnPowerFail, rbnFanIndex=rbnFanIndex, rbnFanStatusEntry=rbnFanStatusEntry, rbnPowerIndex=rbnPowerIndex, rbnEnvMonMIBNotifications=rbnEnvMonMIBNotifications, rbnPowerStatusEntry=rbnPowerStatusEntry, rbnPowerFailChange=rbnPowerFailChange, rbnFanStatusTable=rbnFanStatusTable, rbnEnvMonMIBObjects=rbnEnvMonMIBObjects, rbnFanFailChange=rbnFanFailChange)
