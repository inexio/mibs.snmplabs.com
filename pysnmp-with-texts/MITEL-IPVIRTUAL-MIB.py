#
# PySNMP MIB module MITEL-IPVIRTUAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-IPVIRTUAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Counter32, Gauge32, IpAddress, TimeTicks, NotificationType, Integer32, ObjectIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Counter32", "Gauge32", "IpAddress", "TimeTicks", "NotificationType", "Integer32", "ObjectIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "MibIdentifier", "Bits")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
mitelIpGrpIpVirtualGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4))
mitelIpGrpIpVirtualGroup.setRevisions(('2003-03-24 09:31', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelIpGrpIpVirtualGroup.setRevisionsDescriptions(('Convert to SMIv2', 'IP MIB Version 1.0',))
if mibBuilder.loadTexts: mitelIpGrpIpVirtualGroup.setLastUpdated('200303240931Z')
if mibBuilder.loadTexts: mitelIpGrpIpVirtualGroup.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelIpGrpIpVirtualGroup.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelIpGrpIpVirtualGroup.setDescription('The MITEL IP MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRouterIpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelIpVGrpPortTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1), )
if mibBuilder.loadTexts: mitelIpVGrpPortTable.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpPortTable.setDescription('This table is used to display and configure IP virtual port information. Each logical LAN destination may have one or more IP virtuals.')
mitelIpVGrpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1), ).setIndexNames((0, "MITEL-IPVIRTUAL-MIB", "mitelIpVGrpPortTableNetAddr"), (0, "MITEL-IPVIRTUAL-MIB", "mitelIpVGrpPortTableIfIndex"))
if mibBuilder.loadTexts: mitelIpVGrpPortEntry.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpPortEntry.setDescription('Each entry in this table contains configuration information specific to a single IP interface.')
mitelIpVGrpPortTableNetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIpVGrpPortTableNetAddr.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpPortTableNetAddr.setDescription('The IP address that uniquely identifies this entry.')
mitelIpVGrpPortTableNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpVGrpPortTableNetMask.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpPortTableNetMask.setDescription('The subnet mask assigned to this entry.')
mitelIpVGrpPortTableIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIpVGrpPortTableIfIndex.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpPortTableIfIndex.setDescription('The interface that this virtual is associated with.')
mitelIpVGrpPortTableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelIpVGrpPortTableStatus.setReference('Textual Conventions for Version 2 of the Simple Network Management Protocol (RFC 1443).')
if mibBuilder.loadTexts: mitelIpVGrpPortTableStatus.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpPortTableStatus.setDescription('The current status of this entry.')
mitelIpVGrpPortTableCfgMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("static", 1), ("addressless", 2), ("dhcp", 3), ("ipcp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIpVGrpPortTableCfgMethod.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpPortTableCfgMethod.setDescription("Determines how this virtual interface is configured. `static' and `addressless' indicate that all information is provided by the SNMP manager, while `dhcp' and `ipcp' indicate that some or all of the information is obtained dynamically. `static' and `dhcp' interfaces connect to multipoint networks, in which case the mitelIpVGrpPortTableNetMask indicates the IP subnet on that network. `addressless' and `ipcp' interfaces connect to point-to-point networks, and in these cases the mitelIpVGrpPortTableNetMask is set to 255.255.255.255 and the corresponding IP address is that of the system at the other end of the link.")
mitelIpVGrpRipTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2), )
if mibBuilder.loadTexts: mitelIpVGrpRipTable.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpRipTable.setDescription('This table contains RIP statistics per IP virtual interfaces.')
mitelIpVGrpRipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1), ).setIndexNames((0, "MITEL-IPVIRTUAL-MIB", "mitelIpVGrpTableRipIpAddr"))
if mibBuilder.loadTexts: mitelIpVGrpRipEntry.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpRipEntry.setDescription('Each entry in this table contains RIP statistics specific to a single IP interface.')
mitelIpVGrpTableRipIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIpVGrpTableRipIpAddr.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpTableRipIpAddr.setDescription('The IP Address that uniquely defines this entry')
mitelIpVGrpTableRipRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIpVGrpTableRipRxPkts.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpTableRipRxPkts.setDescription('This object indicates the number of RIP packets regardless of RIP type received on this virtual port.')
mitelIpVGrpTableRipRxBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIpVGrpTableRipRxBadPkts.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpTableRipRxBadPkts.setDescription('This object indicates the number of received packets that contained incorrect header/packet definition (ie: unsupported version(0), non-zero must be zero fields).')
mitelIpVGrpTableRipRxBadRtes = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIpVGrpTableRipRxBadRtes.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpTableRipRxBadRtes.setDescription('This object indicates the number of received packet entries that contained bad route information (ie: unsupported family(AF_INET), bad metric or a bad network address.')
mitelIpVGrpTableRipTxUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIpVGrpTableRipTxUpdates.setStatus('current')
if mibBuilder.loadTexts: mitelIpVGrpTableRipTxUpdates.setDescription('The number of updates sent on this interface.')
mibBuilder.exportSymbols("MITEL-IPVIRTUAL-MIB", mitelIpVGrpPortTable=mitelIpVGrpPortTable, mitelIpVGrpTableRipIpAddr=mitelIpVGrpTableRipIpAddr, mitelIpVGrpTableRipRxBadPkts=mitelIpVGrpTableRipRxBadPkts, mitelIpVGrpPortTableNetAddr=mitelIpVGrpPortTableNetAddr, mitelIpVGrpRipEntry=mitelIpVGrpRipEntry, mitelIpVGrpPortEntry=mitelIpVGrpPortEntry, mitelProprietary=mitelProprietary, mitelIpVGrpTableRipRxBadRtes=mitelIpVGrpTableRipRxBadRtes, mitelRouterIpGroup=mitelRouterIpGroup, mitelPropIpNetworking=mitelPropIpNetworking, PYSNMP_MODULE_ID=mitelIpGrpIpVirtualGroup, mitelIpNetRouter=mitelIpNetRouter, mitelIpVGrpTableRipRxPkts=mitelIpVGrpTableRipRxPkts, mitelIpVGrpTableRipTxUpdates=mitelIpVGrpTableRipTxUpdates, mitelIpVGrpPortTableStatus=mitelIpVGrpPortTableStatus, mitelIpGrpIpVirtualGroup=mitelIpGrpIpVirtualGroup, mitelIpVGrpPortTableIfIndex=mitelIpVGrpPortTableIfIndex, mitelIpVGrpPortTableCfgMethod=mitelIpVGrpPortTableCfgMethod, mitelIpVGrpRipTable=mitelIpVGrpRipTable, mitelIpVGrpPortTableNetMask=mitelIpVGrpPortTableNetMask, mitel=mitel)
