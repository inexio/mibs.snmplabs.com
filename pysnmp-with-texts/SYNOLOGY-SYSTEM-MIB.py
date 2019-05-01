#
# PySNMP MIB module SYNOLOGY-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SYNOLOGY-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:14:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Gauge32, Bits, enterprises, ObjectIdentity, MibIdentifier, Integer32, NotificationType, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Gauge32", "Bits", "enterprises", "ObjectIdentity", "MibIdentifier", "Integer32", "NotificationType", "iso", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
synoSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 1))
synoSystem.setRevisions(('2013-09-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synoSystem.setRevisionsDescriptions(('Second draft.',))
if mibBuilder.loadTexts: synoSystem.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: synoSystem.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synoSystem.setContactInfo('postal: Jay Pan email: jaypan@synology.com')
if mibBuilder.loadTexts: synoSystem.setDescription('Characteristics of the system information')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
systemStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemStatus.setStatus('current')
if mibBuilder.loadTexts: systemStatus.setDescription('Synology system status Each meanings of status represented describe below. Normal(1): System functionals normally. Failed(2): Volume has crashed. ')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
if mibBuilder.loadTexts: temperature.setDescription('Synology system temperature The temperature of Disk Station uses Celsius degree. ')
powerStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatus.setStatus('current')
if mibBuilder.loadTexts: powerStatus.setDescription('Synology power status Each meanings of status represented describe below. Normal(1): All power supplies functional normally. Failed(2): One of power supply has failed. ')
fan = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 4))
systemFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemFanStatus.setStatus('current')
if mibBuilder.loadTexts: systemFanStatus.setDescription('Synology system fan status Each meanings of status represented describe below. Normal(1): All Internal fans functional normally. Failed(2): One of internal fan stopped. ')
cpuFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuFanStatus.setStatus('current')
if mibBuilder.loadTexts: cpuFanStatus.setDescription('Synology cpu fan status Each meanings of status represented describe below. Normal(1): All CPU fans functional normally. Failed(2): One of CPU fan stopped. ')
dsmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 5))
modelName = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: modelName.setStatus('current')
if mibBuilder.loadTexts: modelName.setDescription('The Model name of this NAS')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
if mibBuilder.loadTexts: serialNumber.setDescription('The serial number of this NAS')
version = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: version.setStatus('current')
if mibBuilder.loadTexts: version.setDescription('The version of this DSM')
upgradeAvailable = MibScalar((1, 3, 6, 1, 4, 1, 6574, 1, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upgradeAvailable.setStatus('current')
if mibBuilder.loadTexts: upgradeAvailable.setDescription('This oid is for checking whether there is a latest DSM can be upgraded. Available(1): There is version ready for download. Unavailable(2): The DSM is latest version. Connecting(3): Checking for the latest DSM. Disconnected(4): Failed to connect to server. Others(5): If DSM is upgrading or downloading, the status will show others.')
systemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 6))
systemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 6, 1))
systemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 1, 6, 2))
systemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 1, 6, 1, 1)).setObjects(("SYNOLOGY-SYSTEM-MIB", "systemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systemCompliance = systemCompliance.setStatus('current')
if mibBuilder.loadTexts: systemCompliance.setDescription('The compliance statement for synoSystem entities which implement the SYNOLOGY SYSTEM MIB.')
systemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 1, 6, 2, 1)).setObjects(("SYNOLOGY-SYSTEM-MIB", "systemStatus"), ("SYNOLOGY-SYSTEM-MIB", "temperature"), ("SYNOLOGY-SYSTEM-MIB", "powerStatus"), ("SYNOLOGY-SYSTEM-MIB", "systemFanStatus"), ("SYNOLOGY-SYSTEM-MIB", "cpuFanStatus"), ("SYNOLOGY-SYSTEM-MIB", "modelName"), ("SYNOLOGY-SYSTEM-MIB", "serialNumber"), ("SYNOLOGY-SYSTEM-MIB", "version"), ("SYNOLOGY-SYSTEM-MIB", "upgradeAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    systemGroup = systemGroup.setStatus('current')
if mibBuilder.loadTexts: systemGroup.setDescription('A collection of objects providing basic information of an synology system entity.')
mibBuilder.exportSymbols("SYNOLOGY-SYSTEM-MIB", systemGroup=systemGroup, systemStatus=systemStatus, temperature=temperature, powerStatus=powerStatus, serialNumber=serialNumber, synoSystem=synoSystem, upgradeAvailable=upgradeAvailable, systemFanStatus=systemFanStatus, fan=fan, systemCompliance=systemCompliance, systemConformance=systemConformance, systemCompliances=systemCompliances, systemGroups=systemGroups, version=version, dsmInfo=dsmInfo, PYSNMP_MODULE_ID=synoSystem, cpuFanStatus=cpuFanStatus, modelName=modelName, synology=synology)
