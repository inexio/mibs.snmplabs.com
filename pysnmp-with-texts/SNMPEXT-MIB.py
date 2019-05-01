#
# PySNMP MIB module SNMPEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMPEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
snmpExt, = mibBuilder.importSymbols("APENT-MIB", "snmpExt")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, ModuleIdentity, Unsigned32, ObjectIdentity, NotificationType, TimeTicks, IpAddress, iso, Bits, Integer32, Counter32, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "NotificationType", "TimeTicks", "IpAddress", "iso", "Bits", "Integer32", "Counter32", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
apSnmpExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 22, 1))
if mibBuilder.loadTexts: apSnmpExtMib.setLastUpdated('9707202000Z')
if mibBuilder.loadTexts: apSnmpExtMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apSnmpExtMib.setContactInfo(' Steven Colby Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apSnmpExtMib.setDescription('')
apSnmpExtTrapGeneric = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtTrapGeneric.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtTrapGeneric.setDescription('This object controls the state of Generic trap generation. ArrowPoint supports the following generic traps: 1) Cold start, 2) Warm start, 3) Link down, 4) Link up, 5) SNMP authentication failure. SNMP authentication failure traps can be individually disallowed using the snmpEnableAuthenTraps object.')
apSnmpExtTrapEnterprise = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtTrapEnterprise.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtTrapEnterprise.setDescription('This object controls the state of Enterprise trap generation. RMON event traps are treated as enterprise traps.')
apSnmpExtCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 22, 4), )
if mibBuilder.loadTexts: apSnmpExtCommunityTable.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtCommunityTable.setDescription('A table of SNMP community information used to determine whether read or write access is permitted to the MIBs. A maximum of 5 concurrent communities are supported.')
apSnmpExtCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 22, 4, 1), ).setIndexNames((0, "SNMPEXT-MIB", "apSnmpExtCommunityName"))
if mibBuilder.loadTexts: apSnmpExtCommunityEntry.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtCommunityEntry.setDescription('An SNMP community entry describing one community name')
apSnmpExtCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 22, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSnmpExtCommunityName.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtCommunityName.setDescription('A community name used for SNMP access to this system')
apSnmpExtCommunityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 22, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ro", 0), ("rw", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSnmpExtCommunityType.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtCommunityType.setDescription('The privilge level of the associated community name when accessing this system. A community level of <ro> allows read-only access, a community level of <rw> allows read and write access.')
apSnmpExtCommunityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 22, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSnmpExtCommunityStatus.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtCommunityStatus.setDescription('Status entry for this row ')
apSnmpExtTrapTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 22, 5), )
if mibBuilder.loadTexts: apSnmpExtTrapTable.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtTrapTable.setDescription('')
apSnmpExtTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 22, 5, 1), ).setIndexNames((0, "SNMPEXT-MIB", "apSnmpExtTrapIp"))
if mibBuilder.loadTexts: apSnmpExtTrapEntry.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtTrapEntry.setDescription('This table contains the configured trap hosts. All entries in this table will receive SNMP traps when generated. A maximum of 5 concurrent trap hosts are supported.')
apSnmpExtTrapIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 22, 5, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSnmpExtTrapIp.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtTrapIp.setDescription('An IP Address of a host configured to receive traps')
apSnmpExtTrapCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 22, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSnmpExtTrapCommunity.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtTrapCommunity.setDescription('The community name to use when sending traps to this device')
apSnmpExtTrapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 22, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apSnmpExtTrapStatus.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtTrapStatus.setDescription('Status entry for this row ')
apSnmpExtReloadConfigVal = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtReloadConfigVal.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtReloadConfigVal.setDescription('This object is used to control apSnmpExtReloadSet, which provides a SNMP based reboot capability. When this object is set to 0, SNMP based reboot is not allowed. When this object is set between 1 - (2^32) - 2, the equivalent value must be written to apSnmpExtReloadSet to cause a reboot. When this object is set to (2^32) -1, a reboot may be caused with any write value to apSnmpExtReloadSet. For security purposes this object always returns 0 on read')
apSnmpExtReloadSet = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtReloadSet.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtReloadSet.setDescription('This object provides SNMP based reboot capabilities. The required set value to effect a reboot is explained in apSnmpExtReloadConfigVal.')
apSnmpExtServiceTraps = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtServiceTraps.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtServiceTraps.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with service transition. See the trap definition in the svcExt.mib name apSvcTransitionTrap.')
apSnmpExtLoginFailTraps = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtLoginFailTraps.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtLoginFailTraps.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with FTP/Console/Telnet authentication failure.')
apSnmpExtReloadTraps = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtReloadTraps.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtReloadTraps.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident a system reload')
apSnmpExtLastTrap = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSnmpExtLastTrap.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtLastTrap.setDescription('This object contains a string which details the last trap which was generated in the system')
apSnmpExtRedundancyTraps = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtRedundancyTraps.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtRedundancyTraps.setDescription('This object controls the generation of ArrowPoint enterprise traps on Redundancy state changes.')
apSnmpExtForceDumpConfigVal = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtForceDumpConfigVal.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtForceDumpConfigVal.setDescription('This object is used to control apSnmpExtForceDump, which provides a SNMP based dump capability. When this object is set to 0, SNMP based dumping is not allowed. When this object is set between 1 - (2^32) - 2, the equivalent value must be written to apSnmpExtForceDump to cause a dump. When this object is set to (2^32) -1, a dump may be caused with any write value to apSnmpExtReloadSet. For security purposes this object always returns 0 on read.')
apSnmpExtForceDumpSlot = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtForceDumpSlot.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtForceDumpSlot.setDescription('This object provides SNMP based dumping capabilities on the CS800. This is the slot number of the module to force to dump and then reload. On the cs100 this object is not used. For security purposes this object always returns a 0.')
apSnmpExtForceDumpSubSlot = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtForceDumpSubSlot.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtForceDumpSubSlot.setDescription('This object provides SNMP based dumping capabilities on the CS800. This is the sub-slot number of the module to force to dump and then reload. On the cs100 this object is not used. For security purposes this object always returns a 0.')
apSnmpExtForceDump = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtForceDump.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtForceDump.setDescription('This object provides SNMP based dumping capabilities. Setting this value to non-zero will force a dump and reload the unit. On a cs800 the apSnmpExtForceDumpSlot and apSnmapExtForceDumpSubSlot objects must be set to valid values or the setting of this object is ignored. For security purposes this object always returns a 0. The required set value to effect a reboot is explained in apSnmpExtForceDumpConfigVal.')
apSnmpExtDosSynTraps = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtDosSynTraps.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtDosSynTraps.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with Denial of Service (DOS) SYN attacks. See the trap definition in the flowMgrExt.mib name apFlowMgrExtDosSynTrap.')
apSnmpExtDosLandTraps = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtDosLandTraps.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtDosLandTraps.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with Denial of Service (DOS) LAND attacks. See the trap definition in the flowMgrExt.mib name apFlowMgrExtDosLandTrap.')
apSnmpExtDosIllegalTraps = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtDosIllegalTraps.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtDosIllegalTraps.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with Denial of Service (DOS) Illegal packet format attacks. See the trap definition in the flowMgrExt.mib name apFlowMgrExtDosIllegalTrap.')
apSnmpExtDosPingTraps = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtDosPingTraps.setStatus('obsolete')
if mibBuilder.loadTexts: apSnmpExtDosPingTraps.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with Denial of Service (DOS) Ping of Death attacks. See the trap definition in the flowMgrExt.mib name apFlowMgrExtDosPingTrap.')
apSnmpExtDosSmurfTraps = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtDosSmurfTraps.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtDosSmurfTraps.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with Denial of Service (DOS) Smurf attacks. See the trap definition in the flowMgrExt.mib name apFlowMgrExtDosSmurfTrap.')
apSnmpExtDosSynTrapThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtDosSynTrapThreshold.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtDosSynTrapThreshold.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with Denial of Service (DOS) SYN attacks. It is the threshold over which a trap will be generated.')
apSnmpExtDosLandTrapThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtDosLandTrapThreshold.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtDosLandTrapThreshold.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with Denial of Service (DOS) LAND attacks. It is the threshold over which a trap will be generated.')
apSnmpExtDosIllegalTrapThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtDosIllegalTrapThreshold.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtDosIllegalTrapThreshold.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with Denial of Service (DOS) attacks due to invalid packets. It is the threshold over which a trap will be generated.')
apSnmpExtDosPingTrapThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtDosPingTrapThreshold.setStatus('obsolete')
if mibBuilder.loadTexts: apSnmpExtDosPingTrapThreshold.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with Denial of Service (DOS) Ping of Death attacks. It is the threshold over which a trap will be generated.')
apSnmpExtDosSmurfTrapThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 22, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apSnmpExtDosSmurfTrapThreshold.setStatus('current')
if mibBuilder.loadTexts: apSnmpExtDosSmurfTrapThreshold.setDescription('This object controls the generation of ArrowPoint enterprise traps conincident with Denial of Service (DOS) Smurf attacks. It is the threshold over which a trap will be generated.')
apSnmpExtReloadTrap = NotificationType((1, 3, 6, 1, 4, 1, 2467, 1, 22) + (0,1))
if mibBuilder.loadTexts: apSnmpExtReloadTrap.setDescription('This trap is generated when a reboot of the system is performed.')
mibBuilder.exportSymbols("SNMPEXT-MIB", apSnmpExtLoginFailTraps=apSnmpExtLoginFailTraps, apSnmpExtTrapEntry=apSnmpExtTrapEntry, apSnmpExtDosSynTraps=apSnmpExtDosSynTraps, apSnmpExtForceDump=apSnmpExtForceDump, apSnmpExtDosSynTrapThreshold=apSnmpExtDosSynTrapThreshold, apSnmpExtDosLandTrapThreshold=apSnmpExtDosLandTrapThreshold, apSnmpExtReloadSet=apSnmpExtReloadSet, apSnmpExtTrapTable=apSnmpExtTrapTable, apSnmpExtReloadConfigVal=apSnmpExtReloadConfigVal, apSnmpExtForceDumpConfigVal=apSnmpExtForceDumpConfigVal, apSnmpExtForceDumpSubSlot=apSnmpExtForceDumpSubSlot, apSnmpExtDosPingTraps=apSnmpExtDosPingTraps, apSnmpExtReloadTrap=apSnmpExtReloadTrap, apSnmpExtDosSmurfTrapThreshold=apSnmpExtDosSmurfTrapThreshold, apSnmpExtCommunityType=apSnmpExtCommunityType, apSnmpExtDosPingTrapThreshold=apSnmpExtDosPingTrapThreshold, apSnmpExtMib=apSnmpExtMib, apSnmpExtCommunityEntry=apSnmpExtCommunityEntry, apSnmpExtLastTrap=apSnmpExtLastTrap, apSnmpExtDosIllegalTrapThreshold=apSnmpExtDosIllegalTrapThreshold, apSnmpExtDosLandTraps=apSnmpExtDosLandTraps, apSnmpExtTrapStatus=apSnmpExtTrapStatus, apSnmpExtReloadTraps=apSnmpExtReloadTraps, apSnmpExtDosIllegalTraps=apSnmpExtDosIllegalTraps, PYSNMP_MODULE_ID=apSnmpExtMib, apSnmpExtCommunityName=apSnmpExtCommunityName, apSnmpExtTrapCommunity=apSnmpExtTrapCommunity, apSnmpExtTrapGeneric=apSnmpExtTrapGeneric, apSnmpExtForceDumpSlot=apSnmpExtForceDumpSlot, apSnmpExtTrapEnterprise=apSnmpExtTrapEnterprise, apSnmpExtDosSmurfTraps=apSnmpExtDosSmurfTraps, apSnmpExtCommunityTable=apSnmpExtCommunityTable, apSnmpExtRedundancyTraps=apSnmpExtRedundancyTraps, apSnmpExtTrapIp=apSnmpExtTrapIp, apSnmpExtCommunityStatus=apSnmpExtCommunityStatus, apSnmpExtServiceTraps=apSnmpExtServiceTraps)
