#
# PySNMP MIB module CISCO-COMMON-ROLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-COMMON-ROLES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:53:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, Integer32, TimeTicks, Counter64, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, NotificationType, Gauge32, MibIdentifier, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "TimeTicks", "Counter64", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "NotificationType", "Gauge32", "MibIdentifier", "iso", "Unsigned32")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
ciscoCommonRolesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 361))
ciscoCommonRolesMIB.setRevisions(('2008-02-15 00:00', '2003-09-15 00:00', '2003-06-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCommonRolesMIB.setRevisionsDescriptions(('Added two new types to commonRoleSupportedOperation. Added commonRoleSupportedOperation to ciscoCommonRolesMIBCompliance, to indicate that a device implementing this MIB need not support the two new types. Added ciscoCommonRolesExtMIBCompliance and ccrmConfigurationExtGroup, defining compliance is for entities that implement the CISCO-COMMON-ROLES-EXT-MIB', 'Added DEFVAL to commonRoleRuleFeatureName. Also, removed commonRoleRuleFeatureName from mandatory object list while creating row in the commonRoleRuleTable.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCommonRolesMIB.setLastUpdated('200802150000Z')
if mibBuilder.loadTexts: ciscoCommonRolesMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoCommonRolesMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 -NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoCommonRolesMIB.setDescription("MIB module for managing the common roles between access methods like Command Line Interface (CLI), SNMP and XML interfaces. Every user on a device is associated with a role. A user role defines access rights afforded to the users that belog to this role. A role specifies which commands/operations a user is able to perform on what information. SNMP uses VACM (View-based Access Control Model) group to define access rights. Both SNMPv1/v2c community and SNMPv3 user have to belong to a group in order to access information. CLI uses proprietary mechanisms to define the access rights. Most of them depend on the underlying operating system. Groups created from SNMP are not same as the roles created from CLI unless they are synchronized. In addition to this, views make up the roles in VACM where was some kind of internal rules make the roles in the CLI. This MIB describes a framework in which a role defined independent of access methods. It is up to the the particular access method to convert this framework information into the native information. For example, SNMP needs to convert common role framework to VACM. Note that this framework could be also used for any other access methods other than SNMP and CLI. The framework needs a list of features and list of operations they can support. Features provide the data context and are system dependent. Operations are the actions that can be done on the data. The role are defined in terms of rules. Rules are essentially access rights which specify if a certain operation on a feature is permitted or not. An extension to this MIB module has been defined in CISCO-COMMON-ROLES-EXT-MIB to provide support for a framework which has compound features, i.e., features defined as group of other features, and also to provide another option for how a user's access can be restricted.")
ciscoCommonRolesNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 0))
ciscoCommonRolesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 1))
ciscoCommonRolesMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 2))
ccrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1))
ccrRoleConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2))
ccrRuleConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3))
class CommonRoleOperation(TextualConvention, Integer32):
    description = 'Operations allowed for a common role. clear - Clear operation config - Config/Set operation debug - Debug operation show - Show/Get operation exec - Exec/Set Operation Note that if an operation is not supported by an access method, then it does not apply to that access method.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("clear", 1), ("config", 2), ("debug", 3), ("show", 4), ("exec", 5))

commonRoleFeatureTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1), )
if mibBuilder.loadTexts: commonRoleFeatureTable.setStatus('current')
if mibBuilder.loadTexts: commonRoleFeatureTable.setDescription('This table lists all the features and the operations supported by the features on the system.')
commonRoleFeatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-COMMON-ROLES-MIB", "commonRoleFeatureIndex"))
if mibBuilder.loadTexts: commonRoleFeatureEntry.setStatus('current')
if mibBuilder.loadTexts: commonRoleFeatureEntry.setDescription('An entry (conceptual row) in the commonRoleFeatureTable containing information about features and the operations supported by each of the features.')
commonRoleFeatureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: commonRoleFeatureIndex.setStatus('current')
if mibBuilder.loadTexts: commonRoleFeatureIndex.setDescription('An arbitrary index for this entry.')
commonRoleFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonRoleFeatureName.setStatus('current')
if mibBuilder.loadTexts: commonRoleFeatureName.setDescription("Name of the feature. For example, strings like 'ip', 'snmp-server' and 'vsan' are valid feature names.")
commonRoleFeatureOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 1, 1, 3), CommonRoleOperation()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonRoleFeatureOperation.setStatus('current')
if mibBuilder.loadTexts: commonRoleFeatureOperation.setDescription('The operation associated with this feature.')
commonRoleSupportedOperTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2), )
if mibBuilder.loadTexts: commonRoleSupportedOperTable.setStatus('current')
if mibBuilder.loadTexts: commonRoleSupportedOperTable.setDescription("This table lists all the access methods supported on device and the operations supported by each of the access methods. The operations listed in CommonRoleOperation may not be supported by all the access methods. For example, suppose that in the future, a new operation 'create' is added to CommonRoleOperation. CLI may not support it; but may be supported by XML. So this operation would not apply to CLI. This table captures the supported operations for each of the access methods.")
commonRoleSupportedOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-COMMON-ROLES-MIB", "commonRoleAccessMethod"))
if mibBuilder.loadTexts: commonRoleSupportedOperEntry.setStatus('current')
if mibBuilder.loadTexts: commonRoleSupportedOperEntry.setDescription('An entry (conceptual row) in the commonRoleSupportedOperTable which lists the operations supported by the local device for a particular access method.')
commonRoleAccessMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cli", 1), ("snmp", 2))))
if mibBuilder.loadTexts: commonRoleAccessMethod.setStatus('current')
if mibBuilder.loadTexts: commonRoleAccessMethod.setDescription('Access method supported on this system.')
commonRoleSupportedOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 1, 2, 1, 2), Bits().clone(namedValues=NamedValues(("clear", 0), ("config", 1), ("debug", 2), ("show", 3), ("exec", 4), ("read", 5), ("readWrite", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonRoleSupportedOperation.setStatus('current')
if mibBuilder.loadTexts: commonRoleSupportedOperation.setDescription('Operations supported by the access method. clear - Clear operation config - Config/Set operation debug - Debug operation show - Show/Get operation exec - Exec/Set Operation read - Read operation readWrite - Read/Write operation .')
commonRoleMaxRoles = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonRoleMaxRoles.setStatus('current')
if mibBuilder.loadTexts: commonRoleMaxRoles.setDescription('Maximum number of common roles that can be configured this device. i.e., the maximum number of entries in the commonRoleTable.')
commonRoleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2), )
if mibBuilder.loadTexts: commonRoleTable.setStatus('current')
if mibBuilder.loadTexts: commonRoleTable.setDescription('This table lists all the common roles configured on this device.Common roles are the user roles which are common across SNMP and CLI.')
commonRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-COMMON-ROLES-MIB", "commonRoleName"))
if mibBuilder.loadTexts: commonRoleEntry.setStatus('current')
if mibBuilder.loadTexts: commonRoleEntry.setDescription('An entry (conceptual row) in the commonRoleTable.')
commonRoleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: commonRoleName.setStatus('current')
if mibBuilder.loadTexts: commonRoleName.setDescription('Name of the common role.')
commonRoleDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleDescription.setStatus('current')
if mibBuilder.loadTexts: commonRoleDescription.setDescription('Description of the common role.')
commonRoleScopeRestriction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("vsan", 2))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleScopeRestriction.setStatus('current')
if mibBuilder.loadTexts: commonRoleScopeRestriction.setDescription("This object indicates if there is a scope restriction for this role. If the value of this object is 'none', then there no scope restriction. If it is 'vsan', the two objects commonRoleScope1 and commonRoleScope2 provide the list of Virtual Storage Area Networks (VSANs) which this role can access. The object commonRoleScope1 provides list of VSANs from 0 through 2047 and commonRoleScope2 provides from 2048 through 4095. Each octet within the value of the the two objects specifies a set of eight VSANs. The first octet specifies VSANs 0 through 7 for commonRoleScope1 and VSANs 2048 through 2054 for commonRoleScope2. Similarly, the second octet specifies VSANs 8 through 15 and VSANs 2055 through 2062 for commonRoleScope2, etc. Within each octet, the most significant bit represents the lowest numbered VSAN, and the least significant bit represents the highest numbered VSAN. Thus, each VSAN, is represented by a single bit within the value of this object. A role can access a VSAN if and only if that bit has a value of '1'. If these objects have a value which are less than 256 bytes long, then the VSANs which are not represented are not considered to be in these list. If both the scope objects are zero-length strings, then this role can not access any VSANs if this object is `vsan'. The role can access all the VSANs if the this object is 'none'. Also, both commonRoleScope1 and commonRoleScope2 are invalid if this object is 'none'. Other means of restricting the scope of a role can be defined in the future by extending this object with additional enumerations. Each such addition will define the restriction and any parameters it might have, which might or might not be specified via the corresponding values of commonRoleScope1 and commonRoleScope2.")
commonRoleScope1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 4), OctetString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleScope1.setStatus('current')
if mibBuilder.loadTexts: commonRoleScope1.setDescription('This object provides the scope for the role. The actual meaning of this object depends the value of commonRoleScopeRestriction and is defined in that object.')
commonRoleScope2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 5), OctetString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleScope2.setStatus('current')
if mibBuilder.loadTexts: commonRoleScope2.setDescription('This object provides the scope for the role. The actual meaning of this object depends the value of commonRoleScopeRestriction and is defined in that object.')
commonRoleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleRowStatus.setStatus('current')
if mibBuilder.loadTexts: commonRoleRowStatus.setDescription('Status of this role.')
commonRoleMaxRulesPerRole = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonRoleMaxRulesPerRole.setStatus('current')
if mibBuilder.loadTexts: commonRoleMaxRulesPerRole.setDescription('Maximum number of rules that can be configured for a role.')
commonRoleRuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2), )
if mibBuilder.loadTexts: commonRoleRuleTable.setStatus('current')
if mibBuilder.loadTexts: commonRoleRuleTable.setDescription("This table lists all the rules configured for roles defined in the commonRoleTable. Each rule defines a feature and related access-level which provides either permit or deny access to the feature information. Entries in this table are also created/deleted using commonRoleRuleRowStatus. A row in this table cannot be made 'active' until a value is explicitly provided for that row's instances of following objects : - commonRoleRuleOperation Also, the following objects cannot be modified when 'commonRoleRuleRowStatus' is 'active' : - commonRoleRuleFeatureName - commonRoleRuleOperation - commonRoleRuleOperPermitted To modify the above objects, the entry must be deleted and re-created with new value of above objects.")
commonRoleRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1), ).setIndexNames((0, "CISCO-COMMON-ROLES-MIB", "commonRoleName"), (0, "CISCO-COMMON-ROLES-MIB", "commonRoleRuleIndex"))
if mibBuilder.loadTexts: commonRoleRuleEntry.setStatus('current')
if mibBuilder.loadTexts: commonRoleRuleEntry.setDescription('An entry (conceptual row) in the commonRoleRuleTable.')
commonRoleRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: commonRoleRuleIndex.setStatus('current')
if mibBuilder.loadTexts: commonRoleRuleIndex.setDescription('A sequential number starting from 1, and less than or equal to commonRoleMaxRulesPerRole, which identifies a rule.')
commonRoleRuleFeatureName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleRuleFeatureName.setStatus('current')
if mibBuilder.loadTexts: commonRoleRuleFeatureName.setDescription('Name of the feature. If this is a zero-length string, then this rule applies to all the features supported on the system as enumerated in commonRoleFeatureTable.')
commonRoleRuleOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 3), CommonRoleOperation()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleRuleOperation.setStatus('current')
if mibBuilder.loadTexts: commonRoleRuleOperation.setDescription('The operation permitted for this rule.')
commonRoleRuleOperPermitted = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 4), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleRuleOperPermitted.setStatus('current')
if mibBuilder.loadTexts: commonRoleRuleOperPermitted.setDescription("This object tells if the operation `commonRoleRuleOperation' is permitted on the feature `commonRoleFeatureName'. The operation is permitted if the value of this object is `true'. If the value of the object is 'false', the operation is not permitted.")
commonRoleRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 361, 1, 3, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: commonRoleRuleRowStatus.setStatus('current')
if mibBuilder.loadTexts: commonRoleRuleRowStatus.setDescription('Status of this rule.')
ciscoCommonRolesMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 1))
ciscoCommonRolesMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 2))
ciscoCommonRolesMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 1, 1)).setObjects(("CISCO-COMMON-ROLES-MIB", "ccrmConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonRolesMIBCompliance = ciscoCommonRolesMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoCommonRolesMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO-COMMON-ROLES-MIB (but not the CISCO-COMMON-ROLES-EXT-MIB).')
ciscoCommonRolesExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 1, 2)).setObjects(("CISCO-COMMON-ROLES-MIB", "ccrmConfigurationExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCommonRolesExtMIBCompliance = ciscoCommonRolesExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoCommonRolesExtMIBCompliance.setDescription('The compliance statement for entities that implement the CISCO-COMMON-ROLES-EXT-MIB.')
ccrmConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 2, 1)).setObjects(("CISCO-COMMON-ROLES-MIB", "commonRoleFeatureName"), ("CISCO-COMMON-ROLES-MIB", "commonRoleFeatureOperation"), ("CISCO-COMMON-ROLES-MIB", "commonRoleSupportedOperation"), ("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRoles"), ("CISCO-COMMON-ROLES-MIB", "commonRoleDescription"), ("CISCO-COMMON-ROLES-MIB", "commonRoleScopeRestriction"), ("CISCO-COMMON-ROLES-MIB", "commonRoleScope1"), ("CISCO-COMMON-ROLES-MIB", "commonRoleScope2"), ("CISCO-COMMON-ROLES-MIB", "commonRoleRowStatus"), ("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRulesPerRole"), ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleFeatureName"), ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleOperation"), ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleOperPermitted"), ("CISCO-COMMON-ROLES-MIB", "commonRoleRuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrmConfigurationGroup = ccrmConfigurationGroup.setStatus('current')
if mibBuilder.loadTexts: ccrmConfigurationGroup.setDescription('A collection of objects for Common Roles configuration.')
ccrmConfigurationExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 361, 2, 2, 2)).setObjects(("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRoles"), ("CISCO-COMMON-ROLES-MIB", "commonRoleSupportedOperation"), ("CISCO-COMMON-ROLES-MIB", "commonRoleMaxRulesPerRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ccrmConfigurationExtGroup = ccrmConfigurationExtGroup.setStatus('current')
if mibBuilder.loadTexts: ccrmConfigurationExtGroup.setDescription('A collection of objects for Common Roles configuration that need to be implemented by a device when the device implements the CISCO-COMMON-ROLES-EXT-MIB.')
mibBuilder.exportSymbols("CISCO-COMMON-ROLES-MIB", commonRoleFeatureEntry=commonRoleFeatureEntry, ccrmConfigurationGroup=ccrmConfigurationGroup, commonRoleFeatureOperation=commonRoleFeatureOperation, commonRoleDescription=commonRoleDescription, commonRoleRuleEntry=commonRoleRuleEntry, commonRoleRuleIndex=commonRoleRuleIndex, commonRoleScope1=commonRoleScope1, commonRoleSupportedOperEntry=commonRoleSupportedOperEntry, ccrRuleConfig=ccrRuleConfig, commonRoleRuleOperation=commonRoleRuleOperation, commonRoleRuleOperPermitted=commonRoleRuleOperPermitted, ccrmConfigurationExtGroup=ccrmConfigurationExtGroup, commonRoleRuleTable=commonRoleRuleTable, commonRoleScopeRestriction=commonRoleScopeRestriction, ciscoCommonRolesMIBConformance=ciscoCommonRolesMIBConformance, commonRoleMaxRulesPerRole=commonRoleMaxRulesPerRole, commonRoleAccessMethod=commonRoleAccessMethod, commonRoleSupportedOperation=commonRoleSupportedOperation, ciscoCommonRolesMIBGroups=ciscoCommonRolesMIBGroups, commonRoleFeatureTable=commonRoleFeatureTable, commonRoleRuleFeatureName=commonRoleRuleFeatureName, commonRoleRuleRowStatus=commonRoleRuleRowStatus, commonRoleFeatureIndex=commonRoleFeatureIndex, commonRoleFeatureName=commonRoleFeatureName, ciscoCommonRolesMIBObjects=ciscoCommonRolesMIBObjects, ciscoCommonRolesExtMIBCompliance=ciscoCommonRolesExtMIBCompliance, commonRoleScope2=commonRoleScope2, CommonRoleOperation=CommonRoleOperation, ciscoCommonRolesMIB=ciscoCommonRolesMIB, commonRoleName=commonRoleName, ciscoCommonRolesNotifications=ciscoCommonRolesNotifications, ciscoCommonRolesMIBCompliances=ciscoCommonRolesMIBCompliances, PYSNMP_MODULE_ID=ciscoCommonRolesMIB, ccrInfo=ccrInfo, commonRoleEntry=commonRoleEntry, commonRoleRowStatus=commonRoleRowStatus, ciscoCommonRolesMIBCompliance=ciscoCommonRolesMIBCompliance, ccrRoleConfig=ccrRoleConfig, commonRoleTable=commonRoleTable, commonRoleSupportedOperTable=commonRoleSupportedOperTable, commonRoleMaxRoles=commonRoleMaxRoles)
