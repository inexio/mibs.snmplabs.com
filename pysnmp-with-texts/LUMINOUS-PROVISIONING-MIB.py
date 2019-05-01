#
# PySNMP MIB module LUMINOUS-PROVISIONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LUMINOUS-PROVISIONING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:09:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
LumName, LumDescr, LumPortNum, LumTdmType, LumSlotNum = mibBuilder.importSymbols("LUMINOUS-TC-MIB", "LumName", "LumDescr", "LumPortNum", "LumTdmType", "LumSlotNum")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter64, enterprises, Integer32, Counter32, ObjectName, Gauge32, IpAddress, iso, Unsigned32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter64", "enterprises", "Integer32", "Counter32", "ObjectName", "Gauge32", "IpAddress", "iso", "Unsigned32", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "DateAndTime")
luminous = MibIdentifier((1, 3, 6, 1, 4, 1, 4614))
lumADM = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1))
lumProvisioningMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4614, 1, 2))
lumProvisioningMIB.setRevisions(('1901-06-13 00:00', '1900-08-22 00:00', '1900-07-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lumProvisioningMIB.setRevisionsDescriptions(("1. Change name of T1CrossConnect to TDM CrossConnect, and use TC's from shelf.my 2. Add TdmConnectType attribute", '1.PeekBandwidth description fixed. 2.NonConformingAction for rate limitting added. 3.ConnectionStatus values createAndWait(5) and notInService(2) allowed and descriptions added. 4.Depricated lumADMCrossConnect subtree got actually removed.', '- Description clauses filled in or corrected. - All read-write clauses changed to read-create. An exception is ConnectionStatus that is still read-write to keep row deletion functionality - DEFVAL clause specified where appropriate. - lumTdmConnectionName and lumDPConnectionName objects sizes limited to 80. - Enumeration value of are added to lumTdmConfigParam and lumDPProtectionType (defaults to protected(2))objects - SLC96 redefined through lumTdmConfigParam object values, instead of lumTdmLocalPortNumber.',))
if mibBuilder.loadTexts: lumProvisioningMIB.setLastUpdated('0008220000Z')
if mibBuilder.loadTexts: lumProvisioningMIB.setOrganization('Luminous Networks')
if mibBuilder.loadTexts: lumProvisioningMIB.setContactInfo('Luminous Technical Support Postal: Luminous Networks, 14060 Bubb Road, Cupertino, CA 95014 Tel: +1 408 342 6400 Fax: +1 408 863 1100 E-mail: support@luminous.com')
if mibBuilder.loadTexts: lumProvisioningMIB.setDescription('The Luminous Provisioning MIB contains management information required to provision Luminous PacketWave ports. NOTE: additional settings (like T1 ports setting in DS1 MIB (RFC2495) ) may be required to complement the cross-connect requests in the current MIB.')
lumTdmCrossConnect = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2))
lumTdmCrossConnectTable = MibTable((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1), )
if mibBuilder.loadTexts: lumTdmCrossConnectTable.setStatus('current')
if mibBuilder.loadTexts: lumTdmCrossConnectTable.setDescription('The Luminous TDM Cross Connect Table. This table is used to provision TDM cross connects, including T1, E1, T3 and E3.')
lumTdmCrossConnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1), ).setIndexNames((0, "LUMINOUS-PROVISIONING-MIB", "lumTdmLocalCardSlotId"), (0, "LUMINOUS-PROVISIONING-MIB", "lumTdmLocalPortNumber"))
if mibBuilder.loadTexts: lumTdmCrossConnectEntry.setStatus('current')
if mibBuilder.loadTexts: lumTdmCrossConnectEntry.setDescription("This table can have a variable number of entries(rows), containing cross-connect parameters as seen from this side of the cross-connect. When started for the very first time this table is empty (has no rows present). SNMP manager actions are required to create or delete rows in the table. One row typically represents a cross-connect, as seen from this side of cross-connect. Once created, a row is saved in non-volatile memory, and is guarantied to persist after card/shelf reset or a redundant switchover occurs. The lumTdmConnectionStatus object is used to control the process of dynamic row creation and removal as described in RFC2579. Luminous specific adaptation of RFC2579 RowStatus convention follows: - To create a new cross-connect an SNMP Manager must in the one SNMP SET request supply not yet existing instances of at least those read-create objects that have no DEFVAL clause specified. The lumTdmConnectionStatus object's instance value MUST be either createAndGo(4) or createAndWait(5). If the row does not already exist and request is accepted, the SNMP Agent will respond with positive response where it will set the value of lumTdmConnectionStatus instance equal to active(1) or notInService(2) respectfully. - SNMP Manager is allowed to change existing cross-connect from active(1) to notInService(2) and vice versa. - To remove cross-connect completely an SNMP Manager must in one SNMP SET request supply desired instance of lumTdmConnectionStatus with the value of destroy(6). ")
lumTdmLocalCardSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 1), LumSlotNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmLocalCardSlotId.setStatus('current')
if mibBuilder.loadTexts: lumTdmLocalCardSlotId.setDescription('The slot number occupied by a card on this node containing the port to be connected. This must be a valid slot number.')
lumTdmLocalPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 2), LumPortNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmLocalPortNumber.setStatus('current')
if mibBuilder.loadTexts: lumTdmLocalPortNumber.setDescription('The local port number to be connected. This must be a valid port number.')
lumTdmConnectNodeIP = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 3), IpAddress().clone('0.0.0.0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectNodeIP.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectNodeIP.setDescription('The IP address of the destination node. This is only used when the port is using IP encapsulation.')
lumTdmConnectCardSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 4), LumSlotNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectCardSlotId.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectCardSlotId.setDescription('The slot number of the card in the destination node. ')
lumTdmConnectPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 5), LumPortNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectPortNumber.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectPortNumber.setDescription('The port number on the card in the destination node. ')
lumTdmConnectNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 6), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectNumber.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectNumber.setDescription('An arbitrary positive number the user may specify as a connection identifier.')
lumTdmConnectionName = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 7), LumDescr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectionName.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectionName.setDescription('An arbitrary name that the user may specify as a connection identifier.')
lumTdmConnectionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 8), DateAndTime().clone('00000000000')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectionStartTime.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectionStartTime.setDescription('Currently not used.')
lumTdmConnectionStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 9), DateAndTime().clone('00000000000')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectionStopTime.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectionStopTime.setDescription('Currently not used.')
lumTdmConnectConfigParam = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pointToPoint", 1), ("slc96", 2))).clone('pointToPoint')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumTdmConnectConfigParam.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectConfigParam.setDescription('pointToPoint(1) - indicates normal TDM cross-connect; slc96(2) - no longer supported.')
lumTdmConnectionUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumTdmConnectionUpTime.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectionUpTime.setDescription('The actual time passed since the connection has been established. Supplied by the SNMP Agent.')
lumTdmConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 12), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumTdmConnectionStatus.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectionStatus.setDescription('Connection Status. Used to create, change and remove TDM crossconnect. The format and usage is described in RFC2579. Currently only the following are used : - active(1) - returned after successful createAndGo; also can be set when a change from notInService(2) is desired. - notInService(2) - returned after successful createAndWait(5); also can be set when a change from active(1) (disabling) is desired. - createAndGo(4) for create operation; when successful the resulting state will be transitioned into active(1). - createAndWait(5) - for create only; when successful the resulting state will be transitioned into notInService(2). - destroy(6) for delete operation. This object MUST always be present in any SNMP Manager TDM cross connect request.')
lumTdmConnectType = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 2, 1, 1, 13), LumTdmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumTdmConnectType.setStatus('current')
if mibBuilder.loadTexts: lumTdmConnectType.setDescription('The type of TDM service being carried.')
lumDPProvision = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3))
lumDPProvisionTable = MibTable((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1), )
if mibBuilder.loadTexts: lumDPProvisionTable.setStatus('current')
if mibBuilder.loadTexts: lumDPProvisionTable.setDescription('The Luminous Data Provision Table.')
lumDPProvisionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1), ).setIndexNames((0, "LUMINOUS-PROVISIONING-MIB", "lumDPLocalCardSlotId"), (0, "LUMINOUS-PROVISIONING-MIB", "lumDPLocalPortNumber"), (0, "LUMINOUS-PROVISIONING-MIB", "lumDPConnectNumber"))
if mibBuilder.loadTexts: lumDPProvisionEntry.setStatus('current')
if mibBuilder.loadTexts: lumDPProvisionEntry.setDescription("This table can have a variable number of entries(rows), containing provisioning parameters as seen from this side of the cross-connect. When started for the very first time this table is empty (has no rows present). SNMP manager actions are required to create or delete rows in the table. One row typically represents a provisioning, as seen from this of the connection. Once created, a row is saved in non-volatile memory, and is guarantied to persist after card/shelf reset or a redundant switchover occurs. The lumDPConnectionStatus object is used to controls the process of dynamic row creation, removal and modification, as described in RFC2579. Luminous specific adaptation of RFC2579 RowStatus convention follows: - To create a new provisioning an SNMP Manager must in one SNMP SET request supply not yet existing instances of at least those read-write and read-create DEFVAL clause specified. The lumDPConnectionStatus object's instance value MUST be either createAndGo(4) or createAndWait(5). If the row does not already exist and request is accepted, the SNMP Agent will respond with positive response with the value of lumDPConnectionStatus set to active(1) or notInService(2) respectfully. - SNMP Manager is allowed to change existing provisioning from active(1) to notInService(2) and vice versa. - To remove provisioning completely an SNMP Manager must in one SNMP SET request supply desired instance of lumDPConnectionStatus object with the value of destroy(6).")
lumDPLocalCardSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 1), LumSlotNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPLocalCardSlotId.setStatus('current')
if mibBuilder.loadTexts: lumDPLocalCardSlotId.setDescription('The slot number occupied by a card on this node with the port to be provisioned. SNMP Manager must supply a valid positive number for the instance of this object. SNMP Application writer using this MIB may consider analyzing the value of lumShelfType from LUMINOUS-SHELF-MIB and use internal knowledge of the layout of that shelf type to determine the valid slot values.')
lumDPLocalPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 2), LumPortNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPLocalPortNumber.setStatus('current')
if mibBuilder.loadTexts: lumDPLocalPortNumber.setDescription('The local port number to be provisioned. SNMP Manager must supply a valid positive value to the instance on this object when establishing provisioning. SNMP Application writer using this MIB may consider analyzing the value of lumCardNumbOfPorts from LUMINOUS-SHELF-MIB for the card in this slot to determine a valid range.')
lumDPConnectNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectNumber.setStatus('current')
if mibBuilder.loadTexts: lumDPConnectNumber.setDescription('An arbitrary, unique positive number to distinguish between multiple provisioning established on the same local port. SNMP Provisioning Application is responsible to supply unique instance value of this object per a given lumDPLocalCardSlotId and lumDPLocalPortNumber pair when establishing provisioning.')
lumDPConnectNodeIP = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectNodeIP.setStatus('current')
if mibBuilder.loadTexts: lumDPConnectNodeIP.setDescription("The IP address of the connecting node. When establishing provisioning SNMP Manager must set the value of the instance of this objects to an existing Luminous node'd IP Addess.")
lumDPConnectCardSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 5), LumSlotNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectCardSlotId.setStatus('current')
if mibBuilder.loadTexts: lumDPConnectCardSlotId.setDescription('The slot number occupied by the card in the connecting node. SNMP Manager must supply a valid positive number for the instance of this object. Internal knowledge of shelf layout is required to determine the valid values. SNMP Application writer using this MIB may consider analyzing the value of lumShelfType from LUMINOUS-SHELF-MIB and use internal knowledge of that shelf type layout to determine the valid slot values.')
lumDPConnectPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 6), LumPortNum()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectPortNumber.setStatus('current')
if mibBuilder.loadTexts: lumDPConnectPortNumber.setDescription('The remote port number on the card in the connection node. SNMP Manager must set this field to a valid positive value when establishing provisioning. SNMP Application writer using this MIB may consider analyzing the value of lumCardNumbOfPorts from LUMINOUS-SHELF-MIB for the card in the slot to determine the valid port values.')
lumDPConnectionName = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 7), LumDescr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectionName.setStatus('current')
if mibBuilder.loadTexts: lumDPConnectionName.setDescription('An arbitrary name that the user may wish to specify.')
lumDPConnectionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 8), DateAndTime().clone('00000000000')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectionStartTime.setStatus('current')
if mibBuilder.loadTexts: lumDPConnectionStartTime.setDescription('Currently not used.')
lumDPConnectionStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 9), DateAndTime().clone('00000000000')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConnectionStopTime.setStatus('current')
if mibBuilder.loadTexts: lumDPConnectionStopTime.setDescription('Currently not used.')
lumDPCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("wireModel", 1), ("staticIP", 2), ("dynamicIP", 3))).clone('wireModel')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPCategory.setStatus('current')
if mibBuilder.loadTexts: lumDPCategory.setDescription('Provisioning Category. Indicates the provisioning model.')
lumDPClassOfService = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("bestEffort", 1), ("expressForwarding", 2), ("assuredForwarding", 3))).clone('bestEffort')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPClassOfService.setStatus('current')
if mibBuilder.loadTexts: lumDPClassOfService.setDescription('Supported Class of Services.')
lumDPPeakBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPPeakBandwidth.setStatus('current')
if mibBuilder.loadTexts: lumDPPeakBandwidth.setDescription('Peak Bandwidth in Bits/Sec; -1 indicates autonegotiation enabled.')
lumDPSustainedBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPSustainedBandwidth.setStatus('current')
if mibBuilder.loadTexts: lumDPSustainedBandwidth.setDescription('Sustained Bandwidth in in Bits/Sec; positive number.')
lumDPMaximumBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPMaximumBurstSize.setStatus('current')
if mibBuilder.loadTexts: lumDPMaximumBurstSize.setDescription('Maximum Burst Size. In bytes. A positive number.')
lumDPNonConformingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("markDown", 2), ("drop", 3))).clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPNonConformingAction.setStatus('current')
if mibBuilder.loadTexts: lumDPNonConformingAction.setDescription('Non-Conforming Action. Indicates rate limiting action.')
lumDPProtectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unprotected", 1), ("protected", 2))).clone('protected')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPProtectionType.setStatus('current')
if mibBuilder.loadTexts: lumDPProtectionType.setDescription('Protection type. protected(2) provides protection in the case of ring span failure.')
lumDPFacilityProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPFacilityProtection.setStatus('current')
if mibBuilder.loadTexts: lumDPFacilityProtection.setDescription('TBD.')
lumDPIpPrefix1 = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPIpPrefix1.setStatus('current')
if mibBuilder.loadTexts: lumDPIpPrefix1.setDescription('The first IP address to augment the IP Prefix Table.')
lumDPIpPrefix2 = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 19), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPIpPrefix2.setStatus('current')
if mibBuilder.loadTexts: lumDPIpPrefix2.setDescription('The second IP address to augment the IP Prefix Table.')
lumDPIpPrefix3 = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 20), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPIpPrefix3.setStatus('current')
if mibBuilder.loadTexts: lumDPIpPrefix3.setDescription('The third IP address to augment the IP Prefix Table.')
lumDPConfigFile = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 21), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPConfigFile.setStatus('current')
if mibBuilder.loadTexts: lumDPConfigFile.setDescription('Full qualified path and the file name of the file on NMS to contain a large amount of provisioning data, as IP Prefixes for Static IP Provisioning.')
lumDPVLANId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 22), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPVLANId.setStatus('current')
if mibBuilder.loadTexts: lumDPVLANId.setDescription('VLAN Id. TBD.')
lumDPBufferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 23), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lumDPBufferSize.setStatus('current')
if mibBuilder.loadTexts: lumDPBufferSize.setDescription('A positive number.TBD')
lumDPConnectionUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 24), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumDPConnectionUpTime.setStatus('current')
if mibBuilder.loadTexts: lumDPConnectionUpTime.setDescription('The time past since this provisioning has been established. Supplied by SNMP Agent.')
lumDPConnectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 2, 3, 1, 1, 25), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDPConnectionStatus.setStatus('current')
if mibBuilder.loadTexts: lumDPConnectionStatus.setDescription('Connection Status. Used to create, change and remove Data Port provisioning. The format and usage of RowStatus are described in RFC2579. The following values are supported: - active(1) - returned after successful createAndGo; also can be set when a change from notInService(2) is desired. - notInService(2) - returned after successful createAndWait(5); also can be set when a change from active(1) (disabling) is desired. - createAndGo(4) for create operation; when successful the resulting state will be transitioned into active(1). - createAndWait(5) - for create only; when successful the resulting state will be transitioned into notInService(2). - destroy(6) for delete operation. An instance of this object needs always to be present in any SNMP Manager provisioning request.')
mibBuilder.exportSymbols("LUMINOUS-PROVISIONING-MIB", lumTdmLocalCardSlotId=lumTdmLocalCardSlotId, lumDPClassOfService=lumDPClassOfService, lumDPConnectionStatus=lumDPConnectionStatus, lumDPFacilityProtection=lumDPFacilityProtection, lumDPCategory=lumDPCategory, lumTdmConnectionName=lumTdmConnectionName, lumDPProtectionType=lumDPProtectionType, lumDPConnectionUpTime=lumDPConnectionUpTime, lumDPVLANId=lumDPVLANId, lumDPMaximumBurstSize=lumDPMaximumBurstSize, lumTdmConnectType=lumTdmConnectType, lumTdmCrossConnect=lumTdmCrossConnect, lumDPSustainedBandwidth=lumDPSustainedBandwidth, lumDPIpPrefix1=lumDPIpPrefix1, lumDPConfigFile=lumDPConfigFile, lumTdmConnectCardSlotId=lumTdmConnectCardSlotId, lumTdmConnectionUpTime=lumTdmConnectionUpTime, lumTdmCrossConnectTable=lumTdmCrossConnectTable, lumTdmCrossConnectEntry=lumTdmCrossConnectEntry, lumTdmConnectionStopTime=lumTdmConnectionStopTime, lumDPLocalCardSlotId=lumDPLocalCardSlotId, lumTdmConnectPortNumber=lumTdmConnectPortNumber, lumDPConnectCardSlotId=lumDPConnectCardSlotId, lumProvisioningMIB=lumProvisioningMIB, lumDPLocalPortNumber=lumDPLocalPortNumber, lumDPConnectionStopTime=lumDPConnectionStopTime, lumDPProvisionEntry=lumDPProvisionEntry, lumTdmConnectConfigParam=lumTdmConnectConfigParam, lumTdmConnectNodeIP=lumTdmConnectNodeIP, lumDPIpPrefix2=lumDPIpPrefix2, lumDPConnectNumber=lumDPConnectNumber, lumDPConnectionStartTime=lumDPConnectionStartTime, lumTdmLocalPortNumber=lumTdmLocalPortNumber, lumTdmConnectNumber=lumTdmConnectNumber, lumDPConnectNodeIP=lumDPConnectNodeIP, PYSNMP_MODULE_ID=lumProvisioningMIB, lumTdmConnectionStartTime=lumTdmConnectionStartTime, luminous=luminous, lumDPIpPrefix3=lumDPIpPrefix3, lumDPConnectionName=lumDPConnectionName, lumDPConnectPortNumber=lumDPConnectPortNumber, lumDPProvisionTable=lumDPProvisionTable, lumDPNonConformingAction=lumDPNonConformingAction, lumTdmConnectionStatus=lumTdmConnectionStatus, lumDPProvision=lumDPProvision, lumDPPeakBandwidth=lumDPPeakBandwidth, lumDPBufferSize=lumDPBufferSize, lumADM=lumADM)
