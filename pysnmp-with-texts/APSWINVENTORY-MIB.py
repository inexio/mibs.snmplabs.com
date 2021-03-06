#
# PySNMP MIB module APSWINVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APSWINVENTORY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:24:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, Integer32, IpAddress, Counter32, Counter64, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, NotificationType, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Integer32", "IpAddress", "Counter32", "Counter64", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "NotificationType", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apSwInventoryModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 4))
if mibBuilder.loadTexts: apSwInventoryModule.setLastUpdated('0410181000Z')
if mibBuilder.loadTexts: apSwInventoryModule.setOrganization('Acme Packet, Inc')
if mibBuilder.loadTexts: apSwInventoryModule.setContactInfo(' Customer Service Postal: Acme Packet, Inc 71 Third Avenue Burlington, MA 01803 US Tel: 1-781-328-4400 E-mail: support@acmepacket.com')
if mibBuilder.loadTexts: apSwInventoryModule.setDescription(' The software inventory MIB for Acme Packet')
apSwInventoryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1))
apSwInventoryBootObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1))
apSwInventoryCfgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2))
apSwBootTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1), )
if mibBuilder.loadTexts: apSwBootTable.setStatus('current')
if mibBuilder.loadTexts: apSwBootTable.setDescription('The table of booting software inventory')
apSwBootEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1), ).setIndexNames((0, "APSWINVENTORY-MIB", "apSwBootIndex"))
if mibBuilder.loadTexts: apSwBootEntry.setStatus('current')
if mibBuilder.loadTexts: apSwBootEntry.setDescription('An entry in the software inventory table')
apSwBootIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apSwBootIndex.setStatus('current')
if mibBuilder.loadTexts: apSwBootIndex.setDescription('Unique index for the software inventory table. Index always begins at 1, and increases by 1. The table length depends on the size of software inventory. The index is not associated with any specific inventory entry')
apSwBootDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwBootDescr.setStatus('current')
if mibBuilder.loadTexts: apSwBootDescr.setDescription("Textual description of the software image. It maybe file name, data and time this image was built, or the unique identifier of this software. Examples are: 1. boot image: 10.0.1.12/sd121p3.gz for host address is 10.0.1.12, and image name is sd121p3.gz 2. boot image: /tffs0/sd121p3.gz for boot from flash 0, and image name is sd121p3.gz 3. boot loader: bank0:03/18/2004 10:58:25 for boot from bank 0, and version is 'march 18 2003, 10:58:25' 4. boot loader: <card>:<version>")
apSwBootType = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bootImage", 1), ("bootLoader", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwBootType.setStatus('current')
if mibBuilder.loadTexts: apSwBootType.setDescription('The software entity type')
apSwBootStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("currentUsing", 1), ("previousUsed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwBootStatus.setStatus('current')
if mibBuilder.loadTexts: apSwBootStatus.setDescription('The software entity status')
apSwCfgCurrentVersion = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwCfgCurrentVersion.setStatus('current')
if mibBuilder.loadTexts: apSwCfgCurrentVersion.setDescription('current version of saved configuration')
apSwCfgRunningVersion = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwCfgRunningVersion.setStatus('current')
if mibBuilder.loadTexts: apSwCfgRunningVersion.setDescription('current version of running configuration')
apSwCfgBackuptable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3), )
if mibBuilder.loadTexts: apSwCfgBackuptable.setStatus('current')
if mibBuilder.loadTexts: apSwCfgBackuptable.setDescription('The table of backup configuration files')
apSwCfgBackupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3, 1), ).setIndexNames((0, "APSWINVENTORY-MIB", "apSwCfgBackupIndex"))
if mibBuilder.loadTexts: apSwCfgBackupEntry.setStatus('current')
if mibBuilder.loadTexts: apSwCfgBackupEntry.setDescription('An entry in the backup configuration files table')
apSwCfgBackupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: apSwCfgBackupIndex.setStatus('current')
if mibBuilder.loadTexts: apSwCfgBackupIndex.setDescription('Unique index for the backup configuration files table. Index always begins at 1, and increases by 1. The table length depends on the size of backup configuration. The index is not associated with any specific entry')
apSwCfgBackupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 4, 1, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSwCfgBackupName.setStatus('current')
if mibBuilder.loadTexts: apSwCfgBackupName.setDescription('Textual description of the condifuration file name. Examples are: p1604, 063004-cfg')
apSwInventoryNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 2))
apSwCfgNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 2, 1))
apSwCfgTrapPreviousVersion = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apSwCfgTrapPreviousVersion.setStatus('current')
if mibBuilder.loadTexts: apSwCfgTrapPreviousVersion.setDescription('The previous version before this trap happened')
apSwCfgTrapCurrentVersion = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apSwCfgTrapCurrentVersion.setStatus('current')
if mibBuilder.loadTexts: apSwCfgTrapCurrentVersion.setDescription('The current version after this trap happened')
apSwInventoryNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 3))
apSwInventoryNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 3, 0))
apSwCfgActivateNotification = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 4, 3, 0, 1)).setObjects(("APSWINVENTORY-MIB", "apSwCfgTrapPreviousVersion"), ("APSWINVENTORY-MIB", "apSwCfgTrapCurrentVersion"))
if mibBuilder.loadTexts: apSwCfgActivateNotification.setStatus('current')
if mibBuilder.loadTexts: apSwCfgActivateNotification.setDescription('This trap is sent if <activate-config> is issued and configration has been changed at runnign time')
apSwInventoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4))
apSwInventoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 1))
apSwInventoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 2))
apSwInventoryNotificationsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 3))
apSwBootObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 2, 1)).setObjects(("APSWINVENTORY-MIB", "apSwBootDescr"), ("APSWINVENTORY-MIB", "apSwBootType"), ("APSWINVENTORY-MIB", "apSwBootStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwBootObjectsGroup = apSwBootObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: apSwBootObjectsGroup.setDescription('A collection of objects providing the software booting inventory')
apSwCfgObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 2, 2)).setObjects(("APSWINVENTORY-MIB", "apSwCfgCurrentVersion"), ("APSWINVENTORY-MIB", "apSwCfgRunningVersion"), ("APSWINVENTORY-MIB", "apSwCfgBackupName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwCfgObjectsGroup = apSwCfgObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: apSwCfgObjectsGroup.setDescription('A collection of objects providing the configuraion files')
apSwInventoryNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 4, 4, 3, 1)).setObjects(("APSWINVENTORY-MIB", "apSwCfgActivateNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apSwInventoryNotificationsGroup = apSwInventoryNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: apSwInventoryNotificationsGroup.setDescription('A collection of notifications providing the change for software inventory.')
mibBuilder.exportSymbols("APSWINVENTORY-MIB", apSwCfgCurrentVersion=apSwCfgCurrentVersion, apSwInventoryCompliances=apSwInventoryCompliances, apSwInventoryMIBObjects=apSwInventoryMIBObjects, apSwCfgTrapCurrentVersion=apSwCfgTrapCurrentVersion, apSwCfgBackupEntry=apSwCfgBackupEntry, apSwCfgNotificationObjects=apSwCfgNotificationObjects, apSwInventoryCfgObjects=apSwInventoryCfgObjects, apSwCfgBackupName=apSwCfgBackupName, PYSNMP_MODULE_ID=apSwInventoryModule, apSwCfgTrapPreviousVersion=apSwCfgTrapPreviousVersion, apSwCfgRunningVersion=apSwCfgRunningVersion, apSwCfgBackuptable=apSwCfgBackuptable, apSwInventoryNotificationsGroups=apSwInventoryNotificationsGroups, apSwBootDescr=apSwBootDescr, apSwBootEntry=apSwBootEntry, apSwInventoryNotificationsGroup=apSwInventoryNotificationsGroup, apSwBootIndex=apSwBootIndex, apSwCfgActivateNotification=apSwCfgActivateNotification, apSwInventoryNotifications=apSwInventoryNotifications, apSwInventoryBootObjects=apSwInventoryBootObjects, apSwCfgBackupIndex=apSwCfgBackupIndex, apSwInventoryConformance=apSwInventoryConformance, apSwInventoryModule=apSwInventoryModule, apSwInventoryNotificationObjects=apSwInventoryNotificationObjects, apSwBootObjectsGroup=apSwBootObjectsGroup, apSwInventoryGroups=apSwInventoryGroups, apSwBootTable=apSwBootTable, apSwBootType=apSwBootType, apSwCfgObjectsGroup=apSwCfgObjectsGroup, apSwBootStatus=apSwBootStatus, apSwInventoryNotificationPrefix=apSwInventoryNotificationPrefix)
