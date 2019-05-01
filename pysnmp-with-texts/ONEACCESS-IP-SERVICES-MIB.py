#
# PySNMP MIB module ONEACCESS-IP-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-IP-SERVICES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
oacMIBModules, oacExpIMIp = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacMIBModules", "oacExpIMIp")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Counter32, IpAddress, Counter64, ObjectIdentity, Integer32, Unsigned32, MibIdentifier, NotificationType, iso, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Counter32", "IpAddress", "Counter64", "ObjectIdentity", "Integer32", "Unsigned32", "MibIdentifier", "NotificationType", "iso", "ModuleIdentity", "TimeTicks")
RowStatus, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "DisplayString", "TextualConvention")
oacIpServicesConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 683))
oacIpServicesConfigMIB.setRevisions(('2011-07-29 00:00', '2011-06-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacIpServicesConfigMIB.setRevisionsDescriptions(('Contact updated', 'This MIB defines configuration capabilities relating to IP services : DHCP client, DNS, ARP .',))
if mibBuilder.loadTexts: oacIpServicesConfigMIB.setLastUpdated('201107290000Z')
if mibBuilder.loadTexts: oacIpServicesConfigMIB.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacIpServicesConfigMIB.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacIpServicesConfigMIB.setDescription('fixed compilation issues')
oacIpServicesConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8))
oacIpServicesConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1))
oacIpServicesConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 2))
oacIpServicesDnsConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 1))
oacIpDnsConfigDomainName = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacIpDnsConfigDomainName.setStatus('current')
if mibBuilder.loadTexts: oacIpDnsConfigDomainName.setDescription(' Configuration of the Domain Name.')
oacIpDnsConfigMainAdd = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 1, 2), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacIpDnsConfigMainAdd.setStatus('current')
if mibBuilder.loadTexts: oacIpDnsConfigMainAdd.setDescription('The main domain server IP address')
oacIpDnsConfigSndAdd = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 1, 3), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacIpDnsConfigSndAdd.setStatus('current')
if mibBuilder.loadTexts: oacIpDnsConfigSndAdd.setDescription('The secondary domain server IP address')
oacIpDnsConfigTimeout = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("timeoutValueDefault", 1), ("timeoutValue4", 2), ("timeoutValue12", 3), ("timeoutValue18", 4), ("timeoutValue42", 5), ("timeoutValue90", 6), ("timeoutValue120", 7))).clone('timeoutValueDefault')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacIpDnsConfigTimeout.setStatus('current')
if mibBuilder.loadTexts: oacIpDnsConfigTimeout.setDescription('The duration (default is 150 seconds) to wait for the name server answer')
oacIpServicesDHCPCConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2))
oacDhcpClientAutoRestartAtm = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacDhcpClientAutoRestartAtm.setStatus('current')
if mibBuilder.loadTexts: oacDhcpClientAutoRestartAtm.setDescription(' DHCP Client specific behavior ')
oacDhcpClientBroadcastFlag = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacDhcpClientBroadcastFlag.setStatus('current')
if mibBuilder.loadTexts: oacDhcpClientBroadcastFlag.setDescription('Activation or not of the broadcast flag in DHCP Offer/Ack message, so that the server is made aware if the DHCP packets are unicast or broadcast')
oacDhcpVendorId = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 199))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacDhcpVendorId.setStatus('current')
if mibBuilder.loadTexts: oacDhcpVendorId.setDescription('To include the option 60 within the DISCOVER messages and to append a proprietary vendor-ID string')
oacIpDhcpClientInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4), )
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceTable.setDescription('This table contains the Additional DHCP Client configuration on interfaces. The ifIndex in the INDEX clause identifies the interface where these options are applied.')
oacIpDhcpClientInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceEntry.setDescription('An entry in this table defines the additional option(s) sent by the DHCP Client.')
oacIpDhcpClientInterfaceIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceIfName.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceIfName.setDescription('The name of the interface where the Dhcp Client is associated. Same as ifDescr from IF-MIB')
oacIpDhcpClientInterfaceIgnoreDefRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceIgnoreDefRoute.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceIgnoreDefRoute.setDescription('Do not insert default route in routing table')
oacIpDhcpClientInterfaceLeaseOptLess = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceLeaseOptLess.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceLeaseOptLess.setDescription('Remove lease option 51 parameter')
oacIpDhcpClientInterfaceUserClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceUserClassId.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceUserClassId.setDescription('Insert option 77 user class, if void option 77 is not inserted')
oacIpDhcpClientInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpClientInterfaceRowStatus.setDescription('The row status for this rule.')
oacIpDhcpAddClientInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5), )
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceTable.setDescription('This table contains the DHCP Client configuration on interfaces. The ifIndex in the INDEX clause identifies the interface where the DHCP Client is activated.')
oacIpDhcpAddClientInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceEntry.setDescription('An entry in this table defines the interface where the DHCP Client is activated.')
oacIpDhcpAddClientInterfaceActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceActivate.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceActivate.setDescription('Activate the DHCP Client on the interface.')
oacIpDhcpAddClientInterfaceIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceIfName.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceIfName.setDescription('The name of the interface where the Dhcp Client is associated. Same as ifDescr from IF-MIB')
oacIpDhcpAddClientInterfaceClientId = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceClientId.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceClientId.setDescription('Set of the Client Identifier. The optional argument indicates which MAC address shall be used in the DHCP DISCOVER message. When the optional client-id argument is not present, the DHCP DISCOVER message uses the MAC address of the interface otherwise if present it uses the client-id string value.')
oacIpDhcpAddClientInterfaceHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceHostname.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceHostname.setDescription('Set of the Hostname.')
oacIpDhcpAddClientInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 2, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: oacIpDhcpAddClientInterfaceRowStatus.setDescription('The row status for this rule.')
oacIpServicesArpProxyConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3))
oacIpProxyArpInterfaceConfigTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3, 1), )
if mibBuilder.loadTexts: oacIpProxyArpInterfaceConfigTable.setStatus('current')
if mibBuilder.loadTexts: oacIpProxyArpInterfaceConfigTable.setDescription('This table contains the Proxy ARP configuration on interfaces. The ifIndex in the INDEX clause identifies the interface where Proxy ARP is applied')
oacIpProxyArpInterfaceConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacIpProxyArpInterfaceConfigEntry.setStatus('current')
if mibBuilder.loadTexts: oacIpProxyArpInterfaceConfigEntry.setDescription('An entry in this table defines the interface where the Proxy ARP is configured.')
oacIpProxyArpInterfaceConfigActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacIpProxyArpInterfaceConfigActivate.setStatus('current')
if mibBuilder.loadTexts: oacIpProxyArpInterfaceConfigActivate.setDescription('Activate Proxy Arp.')
oacIpProxyArpInterfaceConfigIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacIpProxyArpInterfaceConfigIfName.setStatus('current')
if mibBuilder.loadTexts: oacIpProxyArpInterfaceConfigIfName.setDescription('The name of the interface where Proxy Arp is activated. Same as ifDescr from IF-MIB')
oacIpProxyArpInterfaceConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacIpProxyArpInterfaceConfigRowStatus.setStatus('current')
if mibBuilder.loadTexts: oacIpProxyArpInterfaceConfigRowStatus.setDescription('The Row Status for this rule.')
oacIpServicesIcmpRedirConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 4))
oacIpIcmpRedirConfigActivate = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 4, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacIpIcmpRedirConfigActivate.setStatus('current')
if mibBuilder.loadTexts: oacIpIcmpRedirConfigActivate.setDescription('Enable ICMP host redirects.')
oacIpIcmpRedirConfigRedirRoutesActivate = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacIpIcmpRedirConfigRedirRoutesActivate.setStatus('current')
if mibBuilder.loadTexts: oacIpIcmpRedirConfigRedirRoutesActivate.setDescription('Enable learning icmp redirect routes. It is possible to define the timeout (in seconds) of redirect routes See below the meaning of the different values : - Default timeout 180s - 0 Value to disable learning icmp redirect routes (default behaviour) - <1-4294967295> Timeout of redirect routes (seconds)')
oacIpIcmpRedirConfigRateLimitUnreach = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 1, 4, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oacIpIcmpRedirConfigRateLimitUnreach.setStatus('current')
if mibBuilder.loadTexts: oacIpIcmpRedirConfigRateLimitUnreach.setDescription('rate limit icmp messages generated. See below the meaning of the different values : - Default value 500ms - 0 Default behaviour - <1-4294967295> Once per milliseconds')
oacIpServicesGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 2, 1))
oacIpServicesConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 2, 1, 1)).setObjects(("ONEACCESS-IP-SERVICES-MIB", "oacIpDnsConfigDomainName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacIpServicesConfigGroup = oacIpServicesConfigGroup.setStatus('current')
if mibBuilder.loadTexts: oacIpServicesConfigGroup.setDescription('Group of IP Servicesobjects')
oacIpServicesCompls = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 8, 2, 2))
mibBuilder.exportSymbols("ONEACCESS-IP-SERVICES-MIB", oacIpServicesIcmpRedirConfigObjects=oacIpServicesIcmpRedirConfigObjects, oacIpServicesConfig=oacIpServicesConfig, oacIpServicesDnsConfigObjects=oacIpServicesDnsConfigObjects, oacIpDhcpClientInterfaceTable=oacIpDhcpClientInterfaceTable, oacIpDhcpClientInterfaceLeaseOptLess=oacIpDhcpClientInterfaceLeaseOptLess, oacIpDhcpClientInterfaceUserClassId=oacIpDhcpClientInterfaceUserClassId, oacIpServicesConfigObjects=oacIpServicesConfigObjects, oacIpDnsConfigDomainName=oacIpDnsConfigDomainName, PYSNMP_MODULE_ID=oacIpServicesConfigMIB, oacIpProxyArpInterfaceConfigActivate=oacIpProxyArpInterfaceConfigActivate, oacIpIcmpRedirConfigActivate=oacIpIcmpRedirConfigActivate, oacIpDnsConfigMainAdd=oacIpDnsConfigMainAdd, oacIpDhcpAddClientInterfaceActivate=oacIpDhcpAddClientInterfaceActivate, oacIpDhcpAddClientInterfaceTable=oacIpDhcpAddClientInterfaceTable, oacIpDhcpClientInterfaceIfName=oacIpDhcpClientInterfaceIfName, oacIpDhcpAddClientInterfaceRowStatus=oacIpDhcpAddClientInterfaceRowStatus, oacIpServicesDHCPCConfigObjects=oacIpServicesDHCPCConfigObjects, oacIpDnsConfigSndAdd=oacIpDnsConfigSndAdd, oacIpIcmpRedirConfigRedirRoutesActivate=oacIpIcmpRedirConfigRedirRoutesActivate, oacIpServicesCompls=oacIpServicesCompls, oacIpProxyArpInterfaceConfigEntry=oacIpProxyArpInterfaceConfigEntry, oacIpProxyArpInterfaceConfigRowStatus=oacIpProxyArpInterfaceConfigRowStatus, oacIpIcmpRedirConfigRateLimitUnreach=oacIpIcmpRedirConfigRateLimitUnreach, oacIpDhcpAddClientInterfaceClientId=oacIpDhcpAddClientInterfaceClientId, oacIpDhcpClientInterfaceRowStatus=oacIpDhcpClientInterfaceRowStatus, oacIpProxyArpInterfaceConfigIfName=oacIpProxyArpInterfaceConfigIfName, oacDhcpClientAutoRestartAtm=oacDhcpClientAutoRestartAtm, oacIpServicesConfigGroup=oacIpServicesConfigGroup, oacIpDhcpAddClientInterfaceEntry=oacIpDhcpAddClientInterfaceEntry, oacIpServicesArpProxyConfigObjects=oacIpServicesArpProxyConfigObjects, oacIpDhcpAddClientInterfaceHostname=oacIpDhcpAddClientInterfaceHostname, oacIpDhcpAddClientInterfaceIfName=oacIpDhcpAddClientInterfaceIfName, oacIpServicesConfigConformance=oacIpServicesConfigConformance, oacIpDhcpClientInterfaceIgnoreDefRoute=oacIpDhcpClientInterfaceIgnoreDefRoute, oacIpProxyArpInterfaceConfigTable=oacIpProxyArpInterfaceConfigTable, oacIpDhcpClientInterfaceEntry=oacIpDhcpClientInterfaceEntry, oacDhcpClientBroadcastFlag=oacDhcpClientBroadcastFlag, oacDhcpVendorId=oacDhcpVendorId, oacIpDnsConfigTimeout=oacIpDnsConfigTimeout, oacIpServicesConfigMIB=oacIpServicesConfigMIB, oacIpServicesGroups=oacIpServicesGroups)
