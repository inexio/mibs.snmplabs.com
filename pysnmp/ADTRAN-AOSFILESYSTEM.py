#
# PySNMP MIB module ADTRAN-AOSFILESYSTEM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-AOSFILESYSTEM
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Counter32, Counter64, ObjectIdentity, Gauge32, TimeTicks, MibIdentifier, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Counter32", "Counter64", "ObjectIdentity", "Gauge32", "TimeTicks", "MibIdentifier", "iso", "NotificationType")
DisplayString, TAddress, TDomain, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TAddress", "TDomain", "RowStatus", "TextualConvention")
adGenAOSFileSystemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 6))
adGenAOSFileSystemMib.setRevisions(('2005-05-18 00:00',))
if mibBuilder.loadTexts: adGenAOSFileSystemMib.setLastUpdated('200505180000Z')
if mibBuilder.loadTexts: adGenAOSFileSystemMib.setOrganization('ADTRAN, Inc.')
adGenAOSFileSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6))
adAOSFileSystemRecordTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1), )
if mibBuilder.loadTexts: adAOSFileSystemRecordTable.setStatus('current')
adAOSFileSystemRecordEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1), ).setIndexNames((0, "ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordID"))
if mibBuilder.loadTexts: adAOSFileSystemRecordEntry.setStatus('current')
adAOSFileSystemRecordID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordID.setStatus('current')
adAOSFileSystemRecordSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordSystem.setStatus('current')
adAOSFileSystemRecordType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("file", 1), ("directory", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordType.setStatus('current')
adAOSFileSystemRecordPath = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordPath.setStatus('current')
adAOSFileSystemRecordName = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordName.setStatus('current')
adAOSFileSystemRecordSize = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordSize.setStatus('current')
adAOSFileSystemRecordStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSFileSystemRecordStatus.setStatus('current')
adAOSFileSystemTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2), )
if mibBuilder.loadTexts: adAOSFileSystemTable.setStatus('current')
adAOSFileSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1), ).setIndexNames((0, "ADTRAN-AOSFILESYSTEM", "adAOSFileSystemID"))
if mibBuilder.loadTexts: adAOSFileSystemEntry.setStatus('current')
adAOSFileSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemID.setStatus('current')
adAOSFileSystemType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemType.setStatus('current')
adAOSFileSystemTotalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemTotalSize.setStatus('current')
adAOSFileSystemFreeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemFreeSize.setStatus('current')
adGenAOSFileSystemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5))
adAOSFileSystemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 1))
adAOSFileSystemRecordGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 2))
adAOSFileSystemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 3))
adAOSFileSystemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 1, 1)).setObjects(("ADTRAN-AOSFILESYSTEM", "adGenAOSFileSystemRecordGroup"), ("ADTRAN-AOSFILESYSTEM", "adGenAOSFileSystemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSFileSystemCompliance = adAOSFileSystemCompliance.setStatus('current')
adGenAOSFileSystemRecordGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 2, 1)).setObjects(("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordID"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordSystem"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordType"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordPath"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordName"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordSize"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFileSystemRecordGroup = adGenAOSFileSystemRecordGroup.setStatus('current')
adGenAOSFileSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 3, 1)).setObjects(("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemID"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemType"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemTotalSize"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemFreeSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFileSystemGroup = adGenAOSFileSystemGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOSFILESYSTEM", adGenAOSFileSystemConformance=adGenAOSFileSystemConformance, adAOSFileSystemCompliance=adAOSFileSystemCompliance, adAOSFileSystemRecordEntry=adAOSFileSystemRecordEntry, adAOSFileSystemRecordPath=adAOSFileSystemRecordPath, adAOSFileSystemType=adAOSFileSystemType, adAOSFileSystemRecordID=adAOSFileSystemRecordID, adAOSFileSystemRecordStatus=adAOSFileSystemRecordStatus, adAOSFileSystemRecordType=adAOSFileSystemRecordType, adAOSFileSystemGroups=adAOSFileSystemGroups, adAOSFileSystemRecordTable=adAOSFileSystemRecordTable, adAOSFileSystemRecordName=adAOSFileSystemRecordName, adAOSFileSystemCompliances=adAOSFileSystemCompliances, adGenAOSFileSystem=adGenAOSFileSystem, adGenAOSFileSystemRecordGroup=adGenAOSFileSystemRecordGroup, adGenAOSFileSystemGroup=adGenAOSFileSystemGroup, adAOSFileSystemRecordSize=adAOSFileSystemRecordSize, adAOSFileSystemID=adAOSFileSystemID, adAOSFileSystemRecordSystem=adAOSFileSystemRecordSystem, PYSNMP_MODULE_ID=adGenAOSFileSystemMib, adAOSFileSystemTable=adAOSFileSystemTable, adAOSFileSystemEntry=adAOSFileSystemEntry, adGenAOSFileSystemMib=adGenAOSFileSystemMib, adAOSFileSystemTotalSize=adAOSFileSystemTotalSize, adAOSFileSystemRecordGroups=adAOSFileSystemRecordGroups, adAOSFileSystemFreeSize=adAOSFileSystemFreeSize)