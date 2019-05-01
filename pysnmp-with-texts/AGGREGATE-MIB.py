#
# PySNMP MIB module AGGREGATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AGGREGATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:15:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, MibIdentifier, Counter64, TimeTicks, IpAddress, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, ObjectIdentity, Opaque, Unsigned32, Bits, ModuleIdentity, experimental = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Counter64", "TimeTicks", "IpAddress", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "ObjectIdentity", "Opaque", "Unsigned32", "Bits", "ModuleIdentity", "experimental")
RowStatus, TextualConvention, DisplayString, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "StorageType")
aggrMIB = ModuleIdentity((1, 3, 6, 1, 3, 123))
aggrMIB.setRevisions(('2006-04-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aggrMIB.setRevisionsDescriptions(('Initial version, published as RFC 4498.',))
if mibBuilder.loadTexts: aggrMIB.setLastUpdated('200604270000Z')
if mibBuilder.loadTexts: aggrMIB.setOrganization('Cyber Solutions Inc. NetMan Working Group')
if mibBuilder.loadTexts: aggrMIB.setContactInfo(' Glenn Mansfield Keeni Postal: Cyber Solutions Inc. 6-6-3, Minami Yoshinari Aoba-ku, Sendai, Japan 989-3204. Tel: +81-22-303-4012 Fax: +81-22-303-4015 E-mail: glenn@cysols.com Support Group E-mail: mibsupport@cysols.com')
if mibBuilder.loadTexts: aggrMIB.setDescription('The MIB for servicing aggregate objects. Copyright (C) The Internet Society (2006). This version of this MIB module is part of RFC 4498; see the RFC itself for full legal notices. ')
class AggrMOErrorStatus(TextualConvention, Opaque):
    description = 'This data type is used to model the error status of the constituent MO instances. The error status for a constituent MO instance is given in terms of two elements: o The moIndex, which indicates the position of the MO instance (starting at 1) in the value of the aggregated MO instance. o The moError, which indicates the error that was encountered in fetching that MO instance. The syntax in ASN.1 Notation will be ErrorStatus :: = SEQUENCE { moIndex Integer32, moError SnmpPduErrorStatus } AggrMOErrorStatus ::= SEQUENCE OF { ErrorStatus } Note1: The command responder will supply values for all constituent MO instances, in the same order in which the MO instances are specified for the AgMO. If an error is encountered for an MO instance, then the corresponding value will have an ASN.1 value NULL, and an error will be flagged in the corresponding AggrMOErrorStatus object. Only MOs for which errors have been encountered will have their corresponding moIndex and moError values set. Note2: The error code for the component MO instances will be in accordance with the SnmpPduErrorStatus TC defined in the DISMAN-SCHEDULE-MIB [RFC3231]. Note3: The command generator will need to know constituent MO instances and their order to correctly interpret AggrMOErrorStatus. '
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(0, 1024)

class AggrMOValue(TextualConvention, Opaque):
    description = "This data type is used to model the aggregate MOs. It will have a format dependent on the constituent MOs, a sequence of values. The syntax in ASN.1 Notation will be MOValue :: = SEQUENCE { value ObjectSyntax } where 'value' is the value of a constituent MO instance. AggrMOValue :: = SEQUENCE OF { MOValue } Note: The command generator will need to know the constituent MO instances and their order to correctly interpret AggrMOValue."
    status = 'current'
    subtypeSpec = Opaque.subtypeSpec + ValueSizeConstraint(0, 1024)

class AggrMOCompressedValue(TextualConvention, OctetString):
    description = 'This data type is used to model the compressed aggregate MOs.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

aggrCtlTable = MibTable((1, 3, 6, 1, 3, 123, 1), )
if mibBuilder.loadTexts: aggrCtlTable.setStatus('current')
if mibBuilder.loadTexts: aggrCtlTable.setDescription('A table that controls the aggregation of the MOs.')
aggrCtlEntry = MibTableRow((1, 3, 6, 1, 3, 123, 1, 1), ).setIndexNames((0, "AGGREGATE-MIB", "aggrCtlEntryID"))
if mibBuilder.loadTexts: aggrCtlEntry.setStatus('current')
if mibBuilder.loadTexts: aggrCtlEntry.setDescription('A row of the control table that defines one aggregated MO. Entries in this table are required to survive a reboot of the managed entity depending on the value of the corresponding aggrCtlEntryStorageType instance. ')
aggrCtlEntryID = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: aggrCtlEntryID.setStatus('current')
if mibBuilder.loadTexts: aggrCtlEntryID.setDescription('A locally unique, administratively assigned name for this aggregated MO. It is used as an index to uniquely identify this row in the table.')
aggrCtlMOIndex = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlMOIndex.setStatus('current')
if mibBuilder.loadTexts: aggrCtlMOIndex.setDescription('A pointer to a group of MOs identified by aggrMOEntryID in the aggrMOTable. This is the group of MOs that will be aggregated.')
aggrCtlMODescr = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlMODescr.setStatus('current')
if mibBuilder.loadTexts: aggrCtlMODescr.setDescription('A textual description of the object that is being aggregated.')
aggrCtlCompressionAlgorithm = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("deflate", 2))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlCompressionAlgorithm.setReference('RFC1951 : DEFLATE Compressed Data Format Specification version 1.3 ')
if mibBuilder.loadTexts: aggrCtlCompressionAlgorithm.setStatus('current')
if mibBuilder.loadTexts: aggrCtlCompressionAlgorithm.setDescription('The compression algorithm that will be used by the agent to compress the value of the aggregated object. The deflate algorithm and corresponding data format specification is described in RFC 1951. It is compatible with the widely used gzip utility. ')
aggrCtlEntryOwner = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 5), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlEntryOwner.setStatus('current')
if mibBuilder.loadTexts: aggrCtlEntryOwner.setDescription('The entity that created this entry.')
aggrCtlEntryStorageType = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlEntryStorageType.setStatus('current')
if mibBuilder.loadTexts: aggrCtlEntryStorageType.setDescription("This object defines whether the parameters defined in this row are kept in volatile storage and lost upon reboot or backed up by non-volatile (permanent) storage. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row. ")
aggrCtlEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 123, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrCtlEntryStatus.setStatus('current')
if mibBuilder.loadTexts: aggrCtlEntryStatus.setDescription("The row status variable, used according to row installation and removal conventions. Objects in a row can be modified only when the value of this object in the corresponding conceptual row is not 'active'. Thus, to modify one or more of the objects in this conceptual row, a. change the row status to 'notInService', b. change the values of the row, and c. change the row status to 'active'. The aggrCtlEntryStatus may be changed to 'active' if all the MOs in the conceptual row have been assigned valid values. ")
aggrMOTable = MibTable((1, 3, 6, 1, 3, 123, 2), )
if mibBuilder.loadTexts: aggrMOTable.setStatus('current')
if mibBuilder.loadTexts: aggrMOTable.setDescription('The table of primary(simple) MOs that will be aggregated. Each row in this table represents a MO that will be aggregated. The aggrMOEntryID index is used to identify the group of MOs that will be aggregated. The aggrMOIndex instance in the corresponding row of the aggrCtlTable will have a value equal to the value of aggrMOEntryID. The aggrMOEntryMOID index is used to identify an MO in the group. ')
aggrMOEntry = MibTableRow((1, 3, 6, 1, 3, 123, 2, 1), ).setIndexNames((0, "AGGREGATE-MIB", "aggrMOEntryID"), (0, "AGGREGATE-MIB", "aggrMOEntryMOID"))
if mibBuilder.loadTexts: aggrMOEntry.setStatus('current')
if mibBuilder.loadTexts: aggrMOEntry.setDescription('A row of the table that specifies one MO. Entries in this table are required to survive a reboot of the managed entity depending on the value of the corresponding aggrMOEntryStorageType instance. ')
aggrMOEntryID = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: aggrMOEntryID.setStatus('current')
if mibBuilder.loadTexts: aggrMOEntryID.setDescription('An index uniquely identifying a group of MOs that will be aggregated.')
aggrMOEntryMOID = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: aggrMOEntryMOID.setStatus('current')
if mibBuilder.loadTexts: aggrMOEntryMOID.setDescription('An index to uniquely identify an MO instance in the group of MO instances that will be aggregated.')
aggrMOInstance = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMOInstance.setStatus('current')
if mibBuilder.loadTexts: aggrMOInstance.setDescription('The OID of the MO instance, the value of which will be sampled by the agent.')
aggrMODescr = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMODescr.setStatus('current')
if mibBuilder.loadTexts: aggrMODescr.setDescription('A textual description of the object that will be aggregated.')
aggrMOEntryStorageType = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 5), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMOEntryStorageType.setStatus('current')
if mibBuilder.loadTexts: aggrMOEntryStorageType.setDescription("This object defines whether the parameters defined in this row are kept in volatile storage and lost upon reboot or backed up by non-volatile (permanent) storage. Conceptual rows having the value 'permanent' need not allow write-access to any columnar objects in the row. ")
aggrMOEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 123, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrMOEntryStatus.setStatus('current')
if mibBuilder.loadTexts: aggrMOEntryStatus.setDescription("The row status variable, used according to row installation and removal conventions. Objects in a row can be modified only when the value of this object in the corresponding conceptual row is not 'active'. Thus, to modify one or more of the objects in this conceptual row, a. change the row status to 'notInService', b. change the values of the row, and c. change the row status to 'active'. The aggrMOEntryStatus may be changed to 'active' iff all the MOs in the conceptual row have been assigned valid values. ")
aggrDataTable = MibTable((1, 3, 6, 1, 3, 123, 3), )
if mibBuilder.loadTexts: aggrDataTable.setStatus('current')
if mibBuilder.loadTexts: aggrDataTable.setDescription('Each row of this table contains information about an aggregateMO indexed by aggrCtlEntryID.')
aggrDataEntry = MibTableRow((1, 3, 6, 1, 3, 123, 3, 1), ).setIndexNames((0, "AGGREGATE-MIB", "aggrCtlEntryID"))
if mibBuilder.loadTexts: aggrDataEntry.setStatus('current')
if mibBuilder.loadTexts: aggrDataEntry.setDescription('Entry containing information pertaining to an aggregate MO.')
aggrDataRecord = MibTableColumn((1, 3, 6, 1, 3, 123, 3, 1, 1), AggrMOValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrDataRecord.setStatus('current')
if mibBuilder.loadTexts: aggrDataRecord.setDescription('The snapshot value of the aggregated MO. Note that the access privileges to this object will be governed by the access privileges of the component objects. Thus, an entity attempting to access an instance of this MO MUST have access rights to all the component instance objects and this MO instance. ')
aggrDataRecordCompressed = MibTableColumn((1, 3, 6, 1, 3, 123, 3, 1, 2), AggrMOCompressedValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrDataRecordCompressed.setStatus('current')
if mibBuilder.loadTexts: aggrDataRecordCompressed.setDescription("The compressed value of the aggregated MO. The compression algorithm will depend on the aggrCtlCompressionAlgorithm given in the corresponding aggrCtlEntry. If the value of the corresponding aggrCtlCompressionAlgorithm is (1) 'none', then the value of all instances of this object will be a string of zero length. Note that the access privileges to this object will be governed by the access privileges of the component objects. Thus, an entity attempting to access an instance of this MO MUST have access rights to all the component instance objects and this MO instance. ")
aggrDataErrorRecord = MibTableColumn((1, 3, 6, 1, 3, 123, 3, 1, 3), AggrMOErrorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrDataErrorRecord.setStatus('current')
if mibBuilder.loadTexts: aggrDataErrorRecord.setDescription('The error status corresponding to the MO instances aggregated in aggrDataRecord (and aggrDataRecordCompressed).')
aggrConformance = MibIdentifier((1, 3, 6, 1, 3, 123, 4))
aggrGroups = MibIdentifier((1, 3, 6, 1, 3, 123, 4, 1))
aggrCompliances = MibIdentifier((1, 3, 6, 1, 3, 123, 4, 2))
aggrMibCompliance = ModuleCompliance((1, 3, 6, 1, 3, 123, 4, 2, 1)).setObjects(("AGGREGATE-MIB", "aggrMibBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aggrMibCompliance = aggrMibCompliance.setStatus('current')
if mibBuilder.loadTexts: aggrMibCompliance.setDescription('The compliance statement for SNMP entities that implement the AGGREGATE-MIB.')
aggrMibBasicGroup = ObjectGroup((1, 3, 6, 1, 3, 123, 4, 1, 1)).setObjects(("AGGREGATE-MIB", "aggrCtlMOIndex"), ("AGGREGATE-MIB", "aggrCtlMODescr"), ("AGGREGATE-MIB", "aggrCtlCompressionAlgorithm"), ("AGGREGATE-MIB", "aggrCtlEntryOwner"), ("AGGREGATE-MIB", "aggrCtlEntryStorageType"), ("AGGREGATE-MIB", "aggrCtlEntryStatus"), ("AGGREGATE-MIB", "aggrMOInstance"), ("AGGREGATE-MIB", "aggrMODescr"), ("AGGREGATE-MIB", "aggrMOEntryStorageType"), ("AGGREGATE-MIB", "aggrMOEntryStatus"), ("AGGREGATE-MIB", "aggrDataRecord"), ("AGGREGATE-MIB", "aggrDataRecordCompressed"), ("AGGREGATE-MIB", "aggrDataErrorRecord"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aggrMibBasicGroup = aggrMibBasicGroup.setStatus('current')
if mibBuilder.loadTexts: aggrMibBasicGroup.setDescription('A collection of objects for aggregation of MOs.')
mibBuilder.exportSymbols("AGGREGATE-MIB", aggrGroups=aggrGroups, aggrCompliances=aggrCompliances, aggrCtlMOIndex=aggrCtlMOIndex, aggrDataEntry=aggrDataEntry, aggrMODescr=aggrMODescr, aggrMIB=aggrMIB, aggrCtlEntryID=aggrCtlEntryID, aggrCtlTable=aggrCtlTable, aggrDataTable=aggrDataTable, aggrMibBasicGroup=aggrMibBasicGroup, aggrDataRecordCompressed=aggrDataRecordCompressed, aggrCtlEntryStorageType=aggrCtlEntryStorageType, AggrMOValue=AggrMOValue, AggrMOErrorStatus=AggrMOErrorStatus, aggrCtlEntry=aggrCtlEntry, aggrDataErrorRecord=aggrDataErrorRecord, aggrMOEntryStatus=aggrMOEntryStatus, aggrMOInstance=aggrMOInstance, aggrCtlEntryOwner=aggrCtlEntryOwner, aggrMOEntry=aggrMOEntry, aggrMOEntryID=aggrMOEntryID, aggrMOEntryStorageType=aggrMOEntryStorageType, aggrCtlCompressionAlgorithm=aggrCtlCompressionAlgorithm, AggrMOCompressedValue=AggrMOCompressedValue, aggrCtlMODescr=aggrCtlMODescr, aggrMOTable=aggrMOTable, aggrDataRecord=aggrDataRecord, aggrConformance=aggrConformance, aggrMOEntryMOID=aggrMOEntryMOID, PYSNMP_MODULE_ID=aggrMIB, aggrMibCompliance=aggrMibCompliance, aggrCtlEntryStatus=aggrCtlEntryStatus)
