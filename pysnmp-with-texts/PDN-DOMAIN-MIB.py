#
# PySNMP MIB module PDN-DOMAIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-DOMAIN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:38:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_domain, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-domain")
VnidTaggingState, VnidRange, SwitchState, ClientState = mibBuilder.importSymbols("PDN-TC", "VnidTaggingState", "VnidRange", "SwitchState", "ClientState")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, ModuleIdentity, Counter64, TimeTicks, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Integer32, Counter32, Gauge32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter64", "TimeTicks", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Integer32", "Counter32", "Gauge32", "iso", "NotificationType")
RowStatus, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "MacAddress")
pdnDomainMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1))
pdnDomainMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 2))
pdnCardGeneralParams = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 1))
pdnCardConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2))
pdnClientConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3))
pdnPortConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4))
pdnCardGeneralParamsVNIDMode = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 1, 1), VnidTaggingState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCardGeneralParamsVNIDMode.setStatus('mandatory')
if mibBuilder.loadTexts: pdnCardGeneralParamsVNIDMode.setDescription('The state of VNID tagging on the card.')
pdnCardConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1), )
if mibBuilder.loadTexts: pdnCardConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: pdnCardConfigTable.setDescription('A table that contains information about Mux Forwarding, IP Filtering, IP Scoping and domain name for each VNID.')
pdnCardConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1), ).setIndexNames((0, "PDN-DOMAIN-MIB", "pdnCardConfigVnidId"))
if mibBuilder.loadTexts: pdnCardConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pdnCardConfigEntry.setDescription('A list of configuration information for each VNID.')
pdnCardConfigVnidId = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 1), VnidRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnCardConfigVnidId.setStatus('mandatory')
if mibBuilder.loadTexts: pdnCardConfigVnidId.setDescription('The VNID Id number of the virtual network for which this entry contains management information.')
pdnCardConfigDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCardConfigDomainName.setStatus('mandatory')
if mibBuilder.loadTexts: pdnCardConfigDomainName.setDescription('The Domain name of the ISP for this VNID. The default value for this object is a blank string')
pdnCardConfigMuxFwd = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 3), SwitchState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCardConfigMuxFwd.setStatus('mandatory')
if mibBuilder.loadTexts: pdnCardConfigMuxFwd.setDescription('This object shows if Mux Forwarding has been enabled or disabled by the user.')
pdnCardConfigIPFiltering = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 4), SwitchState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCardConfigIPFiltering.setStatus('mandatory')
if mibBuilder.loadTexts: pdnCardConfigIPFiltering.setDescription('This object shows if IP Filtering has been enabled or disabled by the user.')
pdnCardConfigIPScoping = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 5), SwitchState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCardConfigIPScoping.setStatus('mandatory')
if mibBuilder.loadTexts: pdnCardConfigIPScoping.setDescription('This object shows if IP Scoping has been enabled or disabled by the user.')
pdnCardConfigVnidAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 6), SwitchState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCardConfigVnidAuth.setStatus('mandatory')
if mibBuilder.loadTexts: pdnCardConfigVnidAuth.setDescription('This object shows if VNID authorization has been enabled or disabled by the user. When this obect is is enable, only interfaces bound to this VNID will accept packets with this VNID.')
pdnCardConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnCardConfigRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: pdnCardConfigRowStatus.setDescription('This object is used to create a new row or or delete an existing row in this table')
pdnPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1), )
if mibBuilder.loadTexts: pdnPortConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: pdnPortConfigTable.setDescription('A table that contains VNID configuration information for each port.')
pdnPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PDN-DOMAIN-MIB", "pdnPortConfigVnidId"))
if mibBuilder.loadTexts: pdnPortConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pdnPortConfigEntry.setDescription('A list of configuration information for each port.')
pdnPortConfigVnidId = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1, 1, 1), VnidRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPortConfigVnidId.setStatus('mandatory')
if mibBuilder.loadTexts: pdnPortConfigVnidId.setDescription('The VNID Id number of the virtual network for which this entry contains management information.')
pdnPortConfigCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("un-bind", 1), ("bind", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnPortConfigCfg.setStatus('mandatory')
if mibBuilder.loadTexts: pdnPortConfigCfg.setDescription('This object shows if a VNID has been binded or not binded to a port.')
pdnPortConfigDefNHR = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnPortConfigDefNHR.setStatus('mandatory')
if mibBuilder.loadTexts: pdnPortConfigDefNHR.setDescription('The Default Next Hop Router address for the specified VNID and port.')
pdnPortConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 4, 1, 1, 4), SwitchState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnPortConfigOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: pdnPortConfigOperStatus.setDescription('This object shows which VNIDs are enabled or disabled for a port.')
pdnClientConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1), )
if mibBuilder.loadTexts: pdnClientConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigTable.setDescription('A table that contains configuration information for each client.')
pdnClientConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PDN-DOMAIN-MIB", "pdnClientConfigAddr"), (0, "PDN-DOMAIN-MIB", "pdnClientConfigSubnetMask"), (0, "PDN-DOMAIN-MIB", "pdnClientConfigVnidId"))
if mibBuilder.loadTexts: pdnClientConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigEntry.setDescription('A list of configuration information for each client.')
pdnClientConfigAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnClientConfigAddr.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigAddr.setDescription('The IP address of the client specified by the client id.')
pdnClientConfigSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnClientConfigSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigSubnetMask.setDescription('The subnet mask of the client.')
pdnClientConfigVnidId = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 3), VnidRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnClientConfigVnidId.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigVnidId.setDescription('The VNID Id number of the virtual network for which this entry contains management information.')
pdnClientConfigNHR = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnClientConfigNHR.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigNHR.setDescription('The Next Hop Router address for the client specified by the client index.')
pdnClientConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 5), ClientState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnClientConfigType.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigType.setDescription('The Configuration type of this entry - Static or Dynamic.')
pdnClientConfigLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnClientConfigLeaseTime.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigLeaseTime.setDescription('The Lease Time in seconds for this client.')
pdnClientConfigLeaseRemainTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnClientConfigLeaseRemainTime.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigLeaseRemainTime.setDescription('The Lease Remaining Time in seconds for this client.')
pdnClientConfigMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 8), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnClientConfigMacAddr.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigMacAddr.setDescription('The MAC Address of the client.')
pdnClientConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 1, 1, 9), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnClientConfigRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientConfigRowStatus.setDescription('This object is used to create a new row or or delete an existing row in this table')
pdnMaxClientsTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 2), )
if mibBuilder.loadTexts: pdnMaxClientsTable.setStatus('mandatory')
if mibBuilder.loadTexts: pdnMaxClientsTable.setDescription('This table contains configuration information for the number of DHCP clients allowed on each DSL interface.')
pdnMaxClientsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnMaxClientsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: pdnMaxClientsEntry.setDescription(' This table is indexed by ifIndex ')
pdnMaxClients = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 2, 1, 1), Integer32().clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMaxClients.setStatus('mandatory')
if mibBuilder.loadTexts: pdnMaxClients.setDescription('This object contains the maximum number of users (static + DHCP) that can be supported by the corresponding xDSL interface. This is in addition to a pool of 256 entries shared among all DSL interfaces')
pdnMaxDynamicClients = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMaxDynamicClients.setStatus('mandatory')
if mibBuilder.loadTexts: pdnMaxDynamicClients.setDescription('This object contains the maximum number of DHCP users that can be supported by the corresponding xDSL interface when IP scoping (connection management) attribute is enabled on the bridge. The valid range for this object is 0 thru pdnMaxClients')
pdnClientAdditionalClientsAvailable = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnClientAdditionalClientsAvailable.setStatus('mandatory')
if mibBuilder.loadTexts: pdnClientAdditionalClientsAvailable.setDescription('This object contains the current number of unallocated client entries')
dhcpClientHostTableFull = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 2) + (0,1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dhcpClientHostTableFull.setDescription("This trap indicates that no more entries can be added to the client VNID table . This trap is of 'warning' class.")
dhcpAddressInStaticSubnet = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 22, 2) + (0,2)).setObjects(("IF-MIB", "ifIndex"), ("PDN-DOMAIN-MIB", "pdnClientConfigSubnetMask"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dhcpAddressInStaticSubnet.setDescription('This trap indicates that the DHCP server attempting to assign an address in range of static subnet on a different port. Information on affected port, subnet mask and the assigned port is also sent with the trap. This trap is of warning class')
mibBuilder.exportSymbols("PDN-DOMAIN-MIB", pdnClientConfigMacAddr=pdnClientConfigMacAddr, pdnCardConfigVnidId=pdnCardConfigVnidId, pdnPortConfigEntry=pdnPortConfigEntry, pdnCardConfigMuxFwd=pdnCardConfigMuxFwd, pdnPortConfigOperStatus=pdnPortConfigOperStatus, pdnCardGeneralParamsVNIDMode=pdnCardGeneralParamsVNIDMode, pdnCardConfigTable=pdnCardConfigTable, pdnPortConfig=pdnPortConfig, pdnCardConfigRowStatus=pdnCardConfigRowStatus, pdnPortConfigDefNHR=pdnPortConfigDefNHR, pdnClientConfigRowStatus=pdnClientConfigRowStatus, pdnClientConfigSubnetMask=pdnClientConfigSubnetMask, pdnClientConfigLeaseRemainTime=pdnClientConfigLeaseRemainTime, pdnClientConfigNHR=pdnClientConfigNHR, pdnCardConfigVnidAuth=pdnCardConfigVnidAuth, pdnClientConfigVnidId=pdnClientConfigVnidId, dhcpClientHostTableFull=dhcpClientHostTableFull, pdnMaxClientsTable=pdnMaxClientsTable, pdnClientConfigAddr=pdnClientConfigAddr, pdnDomainMIBObjects=pdnDomainMIBObjects, pdnCardConfig=pdnCardConfig, pdnClientConfigType=pdnClientConfigType, pdnClientAdditionalClientsAvailable=pdnClientAdditionalClientsAvailable, pdnCardGeneralParams=pdnCardGeneralParams, pdnClientConfigLeaseTime=pdnClientConfigLeaseTime, pdnDomainMIBTraps=pdnDomainMIBTraps, pdnClientConfigEntry=pdnClientConfigEntry, pdnMaxDynamicClients=pdnMaxDynamicClients, dhcpAddressInStaticSubnet=dhcpAddressInStaticSubnet, pdnClientConfigTable=pdnClientConfigTable, pdnCardConfigIPScoping=pdnCardConfigIPScoping, pdnPortConfigVnidId=pdnPortConfigVnidId, pdnClientConfig=pdnClientConfig, pdnCardConfigIPFiltering=pdnCardConfigIPFiltering, pdnCardConfigEntry=pdnCardConfigEntry, pdnPortConfigCfg=pdnPortConfigCfg, pdnCardConfigDomainName=pdnCardConfigDomainName, pdnPortConfigTable=pdnPortConfigTable, pdnMaxClientsEntry=pdnMaxClientsEntry, pdnMaxClients=pdnMaxClients)
