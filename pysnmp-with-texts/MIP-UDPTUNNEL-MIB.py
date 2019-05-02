#
# PySNMP MIB module MIP-UDPTUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MIP-UDPTUNNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:12:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
mipMIB, = mibBuilder.importSymbols("MIP-MIB", "mipMIB")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Counter32, Unsigned32, ModuleIdentity, iso, NotificationType, Counter64, ObjectIdentity, Integer32, MibIdentifier, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Counter32", "Unsigned32", "ModuleIdentity", "iso", "NotificationType", "Counter64", "ObjectIdentity", "Integer32", "MibIdentifier", "TimeTicks", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
mipUdpTunnelMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 44, 4))
mipUdpTunnelMIB.setRevisions(('2007-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mipUdpTunnelMIB.setRevisionsDescriptions(('First version.',))
if mibBuilder.loadTexts: mipUdpTunnelMIB.setLastUpdated('200706120000Z')
if mibBuilder.loadTexts: mipUdpTunnelMIB.setOrganization('IETF Mobility for IPv4 Group')
if mibBuilder.loadTexts: mipUdpTunnelMIB.setContactInfo(' Hans Sjostrand ipUnplugged hans@ipunplugged.com')
if mibBuilder.loadTexts: mipUdpTunnelMIB.setDescription('The MIB module for configuring and displaying Mobile IP Traversal of Network Address Translation (NAT) Devices information. Copyright (C) IETF Trust (2007). This version of this MIB module is part of RFC yyyy; see the RFC itself for full legal notices.')
mipUdpTunnelMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 4, 1))
mnUdpTunnel = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 4, 1, 1))
haUdpTunnel = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 4, 1, 2))
faUdpTunnel = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 4, 1, 3))
mnUdpTunnelEnable = MibScalar((1, 3, 6, 1, 2, 1, 44, 4, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mnUdpTunnelEnable.setStatus('current')
if mibBuilder.loadTexts: mnUdpTunnelEnable.setDescription('This parameter enables and disables the RFC 3519 UDP tunneling function in the MN completely.')
mnUdpTunnelForce = MibScalar((1, 3, 6, 1, 2, 1, 44, 4, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mnUdpTunnelForce.setReference('RFC3519, MIP Traversal of NAT Devices, Section 3.1.1')
if mibBuilder.loadTexts: mnUdpTunnelForce.setStatus('current')
if mibBuilder.loadTexts: mnUdpTunnelForce.setDescription('This parameter enables (or disables) the MN to set the F (force) flag. It indicates that the mobile node wants to use traversal regardless of the outcome of NAT detection performed by the home agent.')
mnUdpTunnelKeepaliveInterval = MibScalar((1, 3, 6, 1, 2, 1, 44, 4, 1, 1, 3), Unsigned32().clone(110)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: mnUdpTunnelKeepaliveInterval.setReference('RFC3519, MIP Traversal of NAT Devices, Section 4.9')
if mibBuilder.loadTexts: mnUdpTunnelKeepaliveInterval.setStatus('current')
if mibBuilder.loadTexts: mnUdpTunnelKeepaliveInterval.setDescription('Defines the default NAT keepalive interval that the mobile node will use in the case that the HA does not impose another value by setting the Keepalive Interval in the UDP Tunnel Reply Extension.')
haUdpTunnelEnable = MibScalar((1, 3, 6, 1, 2, 1, 44, 4, 1, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: haUdpTunnelEnable.setStatus('current')
if mibBuilder.loadTexts: haUdpTunnelEnable.setDescription('This parameter enables and disables the RFC 3519 UDP tunneling function in the HA completely.')
haUdpTunnelKeepaliveInterval = MibScalar((1, 3, 6, 1, 2, 1, 44, 4, 1, 2, 2), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: haUdpTunnelKeepaliveInterval.setReference('RFC3519, MIP Traversal of NAT Devices, Section 3.2')
if mibBuilder.loadTexts: haUdpTunnelKeepaliveInterval.setStatus('current')
if mibBuilder.loadTexts: haUdpTunnelKeepaliveInterval.setDescription('This parameter sets the keepalive interval override. Normally, the MN uses the keepalive time that was configured using UDP tunneling and sending keepalive messages. The HA can override this configured keepalive time by setting a new interval value for this parameter to a value other than zero.')
haUdpTunnelForce = MibScalar((1, 3, 6, 1, 2, 1, 44, 4, 1, 2, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: haUdpTunnelForce.setReference('RFC3519, MIP Traversal of NAT Devices, Section 6.3')
if mibBuilder.loadTexts: haUdpTunnelForce.setStatus('current')
if mibBuilder.loadTexts: haUdpTunnelForce.setDescription('This parameter enables and disables the HA forcing all connections from MNs which support RFC 3519 UDP tunneling to use tunneling whether or not the presence of a NAT is detected.')
haUdpTunnelEncapUnavail = MibScalar((1, 3, 6, 1, 2, 1, 44, 4, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: haUdpTunnelEncapUnavail.setReference('RFC3519, MIP Traversal of NAT Devices, Section 3.5')
if mibBuilder.loadTexts: haUdpTunnelEncapUnavail.setStatus('current')
if mibBuilder.loadTexts: haUdpTunnelEncapUnavail.setDescription('Total number of Registration Requests denied by the home agent -- Requested UDP tunnel encapsulation unavailable (code 142).')
faUdpTunnelEnable = MibScalar((1, 3, 6, 1, 2, 1, 44, 4, 1, 3, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: faUdpTunnelEnable.setStatus('current')
if mibBuilder.loadTexts: faUdpTunnelEnable.setDescription('This parameter enables and disables the RFC 3519 UDP tunneling function in the FA completely.')
faUdpTunnelForce = MibScalar((1, 3, 6, 1, 2, 1, 44, 4, 1, 3, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: faUdpTunnelForce.setReference('RFC3519, MIP Traversal of NAT Devices, Section 3.1.1')
if mibBuilder.loadTexts: faUdpTunnelForce.setStatus('current')
if mibBuilder.loadTexts: faUdpTunnelForce.setDescription('This parameter enables (or disables) the FA to set the F (force) flag. It indicates that the foreign agent wants to use traversal regardless of the outcome of NAT detection performed by the home agent.')
faUdpTunnelKeepaliveInterval = MibScalar((1, 3, 6, 1, 2, 1, 44, 4, 1, 3, 3), Unsigned32().clone(110)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: faUdpTunnelKeepaliveInterval.setReference('RFC3519, MIP Traversal of NAT Devices, Section 4.9')
if mibBuilder.loadTexts: faUdpTunnelKeepaliveInterval.setStatus('current')
if mibBuilder.loadTexts: faUdpTunnelKeepaliveInterval.setDescription('Defines the default NAT keepalive interval that the foreign agent will use in the case that the HA does not impose another value by setting the Keepalive Interval in the UDP Tunnel Reply Extension.')
mipUdpTunnelConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 4, 2))
mipUdpTunnelGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 4, 2, 1))
mipUdpTunnelCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 44, 4, 2, 2))
mipUdpTunnelCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 44, 4, 2, 2, 1)).setObjects(("MIP-UDPTUNNEL-MIB", "mnUdpTunnelGroup"), ("MIP-UDPTUNNEL-MIB", "haUdpTunnelGroup"), ("MIP-UDPTUNNEL-MIB", "faUdpTunnelGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mipUdpTunnelCompliance = mipUdpTunnelCompliance.setStatus('current')
if mibBuilder.loadTexts: mipUdpTunnelCompliance.setDescription('The compliance statement for SNMPv2 entities which implement the Mobile IP UDP Tunnel MIB.')
mnUdpTunnelGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 4, 2, 1, 1)).setObjects(("MIP-UDPTUNNEL-MIB", "mnUdpTunnelEnable"), ("MIP-UDPTUNNEL-MIB", "mnUdpTunnelForce"), ("MIP-UDPTUNNEL-MIB", "mnUdpTunnelKeepaliveInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mnUdpTunnelGroup = mnUdpTunnelGroup.setStatus('current')
if mibBuilder.loadTexts: mnUdpTunnelGroup.setDescription('A collection of objects providing management information for theuse of UDP tunneling according to RFC3519 within a mobile node.')
haUdpTunnelGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 4, 2, 1, 2)).setObjects(("MIP-UDPTUNNEL-MIB", "haUdpTunnelEnable"), ("MIP-UDPTUNNEL-MIB", "haUdpTunnelForce"), ("MIP-UDPTUNNEL-MIB", "haUdpTunnelKeepaliveInterval"), ("MIP-UDPTUNNEL-MIB", "haUdpTunnelEncapUnavail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    haUdpTunnelGroup = haUdpTunnelGroup.setStatus('current')
if mibBuilder.loadTexts: haUdpTunnelGroup.setDescription('A collection of objects providing management information for theuse of UDP tunneling according to RFC3519 within a home agent.')
faUdpTunnelGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 44, 4, 2, 1, 3)).setObjects(("MIP-UDPTUNNEL-MIB", "faUdpTunnelEnable"), ("MIP-UDPTUNNEL-MIB", "faUdpTunnelForce"), ("MIP-UDPTUNNEL-MIB", "faUdpTunnelKeepaliveInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    faUdpTunnelGroup = faUdpTunnelGroup.setStatus('current')
if mibBuilder.loadTexts: faUdpTunnelGroup.setDescription('A collection of objects providing management information for theuse of UDP tunneling according to RFC3519 within a foreign agent.')
mibBuilder.exportSymbols("MIP-UDPTUNNEL-MIB", faUdpTunnel=faUdpTunnel, haUdpTunnelEncapUnavail=haUdpTunnelEncapUnavail, faUdpTunnelKeepaliveInterval=faUdpTunnelKeepaliveInterval, faUdpTunnelEnable=faUdpTunnelEnable, mnUdpTunnelForce=mnUdpTunnelForce, PYSNMP_MODULE_ID=mipUdpTunnelMIB, mnUdpTunnelGroup=mnUdpTunnelGroup, mipUdpTunnelMIB=mipUdpTunnelMIB, faUdpTunnelGroup=faUdpTunnelGroup, faUdpTunnelForce=faUdpTunnelForce, haUdpTunnelForce=haUdpTunnelForce, mipUdpTunnelMIBObjects=mipUdpTunnelMIBObjects, mipUdpTunnelCompliances=mipUdpTunnelCompliances, haUdpTunnelEnable=haUdpTunnelEnable, mipUdpTunnelCompliance=mipUdpTunnelCompliance, haUdpTunnelKeepaliveInterval=haUdpTunnelKeepaliveInterval, mipUdpTunnelGroups=mipUdpTunnelGroups, mnUdpTunnelKeepaliveInterval=mnUdpTunnelKeepaliveInterval, haUdpTunnelGroup=haUdpTunnelGroup, haUdpTunnel=haUdpTunnel, mipUdpTunnelConformance=mipUdpTunnelConformance, mnUdpTunnel=mnUdpTunnel, mnUdpTunnelEnable=mnUdpTunnelEnable)