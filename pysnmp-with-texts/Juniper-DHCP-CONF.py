#
# PySNMP MIB module Juniper-DHCP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DHCP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 14:02:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
juniAgents, = mibBuilder.importSymbols("Juniper-Agents", "juniAgents")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Integer32, NotificationType, Gauge32, Unsigned32, Counter64, TimeTicks, MibIdentifier, Bits, ObjectIdentity, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Integer32", "NotificationType", "Gauge32", "Unsigned32", "Counter64", "TimeTicks", "MibIdentifier", "Bits", "ObjectIdentity", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniDhcpAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8))
juniDhcpAgent.setRevisions(('2007-01-31 20:38', '2005-11-04 19:53', '2005-05-17 19:18', '2005-12-05 21:31', '2004-11-08 16:16', '2004-01-23 16:30', '2003-09-05 19:03', '2002-12-17 16:59', '2002-05-10 19:37', '2001-03-30 18:46',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniDhcpAgent.setRevisionsDescriptions(('Added DHCP Option 60 support, and following objects become obsoleted: rsDhcpLocalServerCableModemServerTable, rsDhcpLocalServerCableModemRequestIn, rsDhcpLocalServerCableModemResponseIn, rsDhcpLocalServerCableModemRequestOut, rsDhcpLocalServerCableModemResponseOut, rsDhcpLocalServerCableModemRequestDropped, rsDhcpLocalServerCableModemResponseDropped, rsDhcpLocalServerCableModemRequestBad, rsDhcpLocalServerCableModemResponseBad, rsDhcpLocalServerCableModemRequestDeleted, rsDhcpLocalServerCableModemPacketsIn, rsDhcpLocalServerCableModemPacketsOut, rsDhcpLocalServerCableModemPacketsDropped. Added juniDhcpRelayBroadcastFlagReplies to control unicast/broadcast delivery of DHCP reply packets. Added juniDhcpRelayGiaddrSelectsInterface for enable/diable of DHCP Relay Giaddr Selects Interface operation mode.', 'Added new DHCP Relay statistics to rsDhcpRelayScalars.', 'Added juniDhcpLocalServerSubInterfaceTable.', 'Added juniDhcpLocalServerBindingsLeaseInterval, juniDhcpLocalServerBindingsLeaseStartTime and juniDhcpLocalServerBindingsInitialLeaseStartTime. Update definition of juniDhcpLocalServerBindingsExpireTime. Added juniDhcpLocalServerBindingsRowStatus to permit administrative clearing of an address binding. Added juniDhcpLocalServerPoolSharedInUse to indicate sharing of DHCP pool addresses. Added statistics for renews, rebinds, errors, and discards. Added juniDhcpRelayLayer2UnicastReplies to control L2 ucast L3 bcast of DHCP reply packets.', 'Added ability to administratively delete DHCP local server address bindings.', 'Added DHCP local server pool exhaustion variables and notifications for high pool utilization and pool exhaustion.', 'Added support to exclude the subinterafce ID from option 82 circuit ID.', 'Replaced Unisphere names with Juniper names. Added host name and virtual router name to the relay agent circuit ID.', 'Added local server reservation and cable modem support. Refined agent info enable into agent circuit ID enable and agent remote ID enable.', 'The initial release of this management information module.',))
if mibBuilder.loadTexts: juniDhcpAgent.setLastUpdated('200701312038Z')
if mibBuilder.loadTexts: juniDhcpAgent.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniDhcpAgent.setContactInfo(' Juniper Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886-3146 USA Tel: +1 978 589 5800 E-mail: mib@Juniper.net')
if mibBuilder.loadTexts: juniDhcpAgent.setDescription('The agent capabilities definitions for the DHCP component of the SNMP agent in the Juniper E-series family of products. The DHCP application has subcomponents that run independently of each other and therefore have separate agent capabilities definitions.')
juniDhcpRelayAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1))
if mibBuilder.loadTexts: juniDhcpRelayAgent.setStatus('current')
if mibBuilder.loadTexts: juniDhcpRelayAgent.setDescription('The DHCP relay subcomponent of the DHCP application. MIB support for each subcomponent can run independently of the other subcomponents.')
juniDhcpRelayAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV1 = juniDhcpRelayAgentV1.setProductRelease('Version 1 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent was supported in JUNOSe 1.3\n        thru 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV1 = juniDhcpRelayAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpRelayAgentV1.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe. These capabilities became obsolete when the agent info enable was refined.')
juniDhcpRelayAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV2 = juniDhcpRelayAgentV2.setProductRelease('Version 2 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent was supported in JUNOSe 4.x\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV2 = juniDhcpRelayAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpRelayAgentV2.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe. These capabilities became obsolete when host name and virtual router name support was added.')
juniDhcpRelayAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV3 = juniDhcpRelayAgentV3.setProductRelease('Version 3 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent was supported in JUNOSe 5.0\n        system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV3 = juniDhcpRelayAgentV3.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpRelayAgentV3.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe. These capabilities became obsolete when support was added for excluding the subinterface ID from option 82 circuit ID.')
juniDhcpRelayAgentV4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV4 = juniDhcpRelayAgentV4.setProductRelease('Version 4 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 5.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV4 = juniDhcpRelayAgentV4.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpRelayAgentV4.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
juniDhcpRelayAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV5 = juniDhcpRelayAgentV5.setProductRelease('Version 5 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 6.1\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV5 = juniDhcpRelayAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpRelayAgentV5.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
juniDhcpRelayAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV6 = juniDhcpRelayAgentV6.setProductRelease('Version 6 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 7.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV6 = juniDhcpRelayAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpRelayAgentV6.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
juniDhcpRelayAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV7 = juniDhcpRelayAgentV7.setProductRelease('Version 7 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 7.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV7 = juniDhcpRelayAgentV7.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpRelayAgentV7.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
juniDhcpRelayAgentV8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV8 = juniDhcpRelayAgentV8.setProductRelease('Version 8 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 7.2\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV8 = juniDhcpRelayAgentV8.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpRelayAgentV8.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
juniDhcpRelayAgentV9 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 1, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV9 = juniDhcpRelayAgentV9.setProductRelease('Version 9 of the DHCP relay subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP relay subcomponent is supported in JUNOSe 8.0\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpRelayAgentV9 = juniDhcpRelayAgentV9.setStatus('current')
if mibBuilder.loadTexts: juniDhcpRelayAgentV9.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
juniDhcpProxyAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2))
if mibBuilder.loadTexts: juniDhcpProxyAgent.setStatus('current')
if mibBuilder.loadTexts: juniDhcpProxyAgent.setDescription('The DHCP proxy subcomponent of the DHCP application. MIB support for each subcomponent can run independently of the other subcomponents.')
juniDhcpProxyAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 2, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpProxyAgentV1 = juniDhcpProxyAgentV1.setProductRelease('Version 1 of the DHCP proxy subcomponent of the JUNOSe SNMP agent.\n        This version of the DHCP proxy subcomponent is supported in JUNOSe 1.3\n        and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpProxyAgentV1 = juniDhcpProxyAgentV1.setStatus('current')
if mibBuilder.loadTexts: juniDhcpProxyAgentV1.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
juniDhcpLocalServerAgent = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3))
if mibBuilder.loadTexts: juniDhcpLocalServerAgent.setStatus('current')
if mibBuilder.loadTexts: juniDhcpLocalServerAgent.setDescription('The DHCP local server subcomponent of the DHCP application. MIB support for each subcomponent can run independently of the other subcomponents.')
juniDhcpLocalServerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV1 = juniDhcpLocalServerAgentV1.setProductRelease('Version 1 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent was supported in\n        JUNOSe 3.1 and subsequent 3.x system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV1 = juniDhcpLocalServerAgentV1.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpLocalServerAgentV1.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe. These capabilities became obsolete when support was added for reservations and cable modems.')
juniDhcpLocalServerAgentV2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV2 = juniDhcpLocalServerAgentV2.setProductRelease('Version 2 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent was supported in\n        JUNOSe 4.0 through 5.1 system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV2 = juniDhcpLocalServerAgentV2.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpLocalServerAgentV2.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe. These capabilities became obsolete when support was added for pool utilization.')
juniDhcpLocalServerAgentV3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV3 = juniDhcpLocalServerAgentV3.setProductRelease('Version 3 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent is supported in\n        JUNOSe 5.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV3 = juniDhcpLocalServerAgentV3.setStatus('current')
if mibBuilder.loadTexts: juniDhcpLocalServerAgentV3.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
juniDhcpLocalServerAgentV5 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV5 = juniDhcpLocalServerAgentV5.setProductRelease('Version 5 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent is supported in\n        JUNOSe 6.2 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV5 = juniDhcpLocalServerAgentV5.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpLocalServerAgentV5.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
juniDhcpLocalServerAgentV6 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV6 = juniDhcpLocalServerAgentV6.setProductRelease('Version 6 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent is supported in\n        JUNOSe 7.1 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV6 = juniDhcpLocalServerAgentV6.setStatus('obsolete')
if mibBuilder.loadTexts: juniDhcpLocalServerAgentV6.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
juniDhcpLocalServerAgentV7 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 8, 3, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV7 = juniDhcpLocalServerAgentV7.setProductRelease('Version 7 of the DHCP local server subcomponent of JUNOSe SNMP agent.\n        This version of the DHCP local server subcomponent is supported in\n        JUNOSe 8.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDhcpLocalServerAgentV7 = juniDhcpLocalServerAgentV7.setStatus('current')
if mibBuilder.loadTexts: juniDhcpLocalServerAgentV7.setDescription('The MIB supported by the SNMP agent for the DHCP application in JUNOSe.')
mibBuilder.exportSymbols("Juniper-DHCP-CONF", juniDhcpLocalServerAgentV1=juniDhcpLocalServerAgentV1, juniDhcpLocalServerAgentV3=juniDhcpLocalServerAgentV3, juniDhcpRelayAgentV9=juniDhcpRelayAgentV9, juniDhcpProxyAgent=juniDhcpProxyAgent, juniDhcpRelayAgentV2=juniDhcpRelayAgentV2, juniDhcpRelayAgentV4=juniDhcpRelayAgentV4, juniDhcpRelayAgentV8=juniDhcpRelayAgentV8, juniDhcpRelayAgentV7=juniDhcpRelayAgentV7, juniDhcpLocalServerAgent=juniDhcpLocalServerAgent, juniDhcpRelayAgent=juniDhcpRelayAgent, juniDhcpLocalServerAgentV5=juniDhcpLocalServerAgentV5, PYSNMP_MODULE_ID=juniDhcpAgent, juniDhcpAgent=juniDhcpAgent, juniDhcpProxyAgentV1=juniDhcpProxyAgentV1, juniDhcpLocalServerAgentV6=juniDhcpLocalServerAgentV6, juniDhcpRelayAgentV1=juniDhcpRelayAgentV1, juniDhcpLocalServerAgentV2=juniDhcpLocalServerAgentV2, juniDhcpLocalServerAgentV7=juniDhcpLocalServerAgentV7, juniDhcpRelayAgentV6=juniDhcpRelayAgentV6, juniDhcpRelayAgentV5=juniDhcpRelayAgentV5, juniDhcpRelayAgentV3=juniDhcpRelayAgentV3)
