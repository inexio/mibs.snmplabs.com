#
# PySNMP MIB module PANASAS-VOLUMES-MIB-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANASAS-VOLUMES-MIB-V1
# Produced by pysmi-0.3.4 at Wed May  1 14:37:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
panFs, = mibBuilder.importSymbols("PANASAS-PANFS-MIB-V1", "panFs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Gauge32, MibIdentifier, TimeTicks, NotificationType, ModuleIdentity, Counter64, iso, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Gauge32", "MibIdentifier", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter64", "iso", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
panVol = ModuleIdentity((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4))
panVol.setRevisions(('2011-04-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panVol.setRevisionsDescriptions(('1. Changed Panasas, Inc. company contact information.',))
if mibBuilder.loadTexts: panVol.setLastUpdated('201104070000Z')
if mibBuilder.loadTexts: panVol.setOrganization('Panasas, Inc')
if mibBuilder.loadTexts: panVol.setContactInfo('postal: Panasas, Inc 969 W. Maude Avenue Sunnyvale, CA 94085 phone: +1 408 215-6800 email: info@panasas.com')
if mibBuilder.loadTexts: panVol.setDescription('This file defines the structure of the panasas system v1 mib.')
panVolTable = MibTable((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1), )
if mibBuilder.loadTexts: panVolTable.setStatus('current')
if mibBuilder.loadTexts: panVolTable.setDescription('A table of volumes in the file system.')
panVolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1), ).setIndexNames((0, "PANASAS-VOLUMES-MIB-V1", "panVolPath"))
if mibBuilder.loadTexts: panVolEntry.setStatus('current')
if mibBuilder.loadTexts: panVolEntry.setDescription('An entry in panVolTable.')
panVolPath = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panVolPath.setStatus('current')
if mibBuilder.loadTexts: panVolPath.setDescription('Full path for volume.')
panVolBladeSet = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panVolBladeSet.setStatus('current')
if mibBuilder.loadTexts: panVolBladeSet.setDescription('Bladeset that the volume is contained in.')
panVolSoftQuota = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panVolSoftQuota.setStatus('current')
if mibBuilder.loadTexts: panVolSoftQuota.setDescription('Soft quota for the volume in Giga Bytes (GB).')
panVolHardQuota = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panVolHardQuota.setStatus('current')
if mibBuilder.loadTexts: panVolHardQuota.setDescription('Hard quota for the volume in Giga Bytes (GB).')
panVolUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panVolUsed.setStatus('current')
if mibBuilder.loadTexts: panVolUsed.setDescription('Capacity used by the volume in Giga Bytes (GB).')
panVolRaid = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panVolRaid.setStatus('current')
if mibBuilder.loadTexts: panVolRaid.setDescription('Is RAID enabled for the volume?')
panVolInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panVolInfo.setStatus('current')
if mibBuilder.loadTexts: panVolInfo.setDescription('Status of the volume.')
mibBuilder.exportSymbols("PANASAS-VOLUMES-MIB-V1", panVolEntry=panVolEntry, panVolRaid=panVolRaid, panVolBladeSet=panVolBladeSet, panVolInfo=panVolInfo, panVolUsed=panVolUsed, panVolHardQuota=panVolHardQuota, PYSNMP_MODULE_ID=panVol, panVol=panVol, panVolSoftQuota=panVolSoftQuota, panVolPath=panVolPath, panVolTable=panVolTable)
