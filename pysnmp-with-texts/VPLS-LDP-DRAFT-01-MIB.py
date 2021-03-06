#
# PySNMP MIB module VPLS-LDP-DRAFT-01-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPLS-LDP-DRAFT-01-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
jnxExperiment, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxExperiment")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, ModuleIdentity, Counter64, Counter32, TimeTicks, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, NotificationType, MibIdentifier, ObjectIdentity, transmission, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Counter64", "Counter32", "TimeTicks", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "NotificationType", "MibIdentifier", "ObjectIdentity", "transmission", "Bits")
StorageType, TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
jnxVplsConfigIndex, jnxVplsPwBindIndex = mibBuilder.importSymbols("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex", "jnxVplsPwBindIndex")
jnxVplsLdpDraft01MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 5, 9))
jnxVplsLdpDraft01MIB.setRevisions(('2006-08-30 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxVplsLdpDraft01MIB.setRevisionsDescriptions(('Initial version published as part of RFC YYYY.',))
if mibBuilder.loadTexts: jnxVplsLdpDraft01MIB.setLastUpdated('200608301200Z')
if mibBuilder.loadTexts: jnxVplsLdpDraft01MIB.setOrganization('Layer 2 Virtual Private Networks (L2VPN) Working Group')
if mibBuilder.loadTexts: jnxVplsLdpDraft01MIB.setContactInfo(' Thomas D. Nadeau Email: tnadeau@cisco.com The L2VPN Working Group (email distribution l2vpn@ietf.org, http://www.ietf.org/html.charters/l2vpn-charter.html) ')
if mibBuilder.loadTexts: jnxVplsLdpDraft01MIB.setDescription('Copyright (C) The IETF Trust (2010). The initial version of this MIB module was published in RFC XXXX. -- RFC Editor: Please replace XXXX with RFC number & remove -- this note. For full legal notices see the RFC itself or see: http://www.ietf.org/copyrights/ianamib.html This MIB module contains managed object definitions for LDP signalled Virtual Private LAN Services as in [RFC4762] This MIB module enables the use of any underlying PseudoWire network. ')
jnxVplsLdpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 9, 0))
jnxVplsLdpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 9, 1))
jnxVplsLdpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 9, 2))
jnxVplsLdpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 1), )
if mibBuilder.loadTexts: jnxVplsLdpConfigTable.setStatus('current')
if mibBuilder.loadTexts: jnxVplsLdpConfigTable.setDescription('This table specifies information for configuring and monitoring LDP specific parameters for Virtual Private Lan Services(VPLS).')
jnxVplsLdpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 1, 1), ).setIndexNames((0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"))
if mibBuilder.loadTexts: jnxVplsLdpConfigEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVplsLdpConfigEntry.setDescription('A row in this table represents LDP specific information for Virtual Private Lan Service(VPLS) in a packet network. It is indexed by jnxVplsConfigIndex, which uniquely identifies a single VPLS. A row is automatically created when a VPLS service is configured using LDP signalling. None of the read-create objects values can be changed when jnxVplsRowStatus is in the active(1) state. Changes are allowed when the jnxVplsRowStatus is in notInService(2) or notReady(3) states only. If the operator need to change one of the values for an active row the jnxVplsConfigRowStatus should be first changed to notInService(2), the objects may be changed now, and later to active(1) in order to re-initiate the signaling process with the new values in effect. ')
jnxVplsLdpConfigMacAddrWithdraw = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsLdpConfigMacAddrWithdraw.setStatus('current')
if mibBuilder.loadTexts: jnxVplsLdpConfigMacAddrWithdraw.setDescription('This object specifies if MAC address withdrawal is enabled in this service. If this object is true then Mac address withdrawl Learning is enabled. If false, then Mac Learning is disabled.')
jnxVplsLdpPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 2), )
if mibBuilder.loadTexts: jnxVplsLdpPwBindTable.setStatus('current')
if mibBuilder.loadTexts: jnxVplsLdpPwBindTable.setDescription('This table provides LDP specific information for an association between a VPLS service and the corresponding Pseudo Wires. A service can have more than one Pseudo Wire association. Pseudo Wires are defined in the pwTable.')
jnxVplsLdpPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 2, 1), ).setIndexNames((0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"), (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsPwBindIndex"))
if mibBuilder.loadTexts: jnxVplsLdpPwBindEntry.setStatus('current')
if mibBuilder.loadTexts: jnxVplsLdpPwBindEntry.setDescription('Each row represents an association between a VPLS instance and one or more Pseudo Wires defined in the pwTable. Each index is unique in describing an entry in this table. However both indexes are required to define the one to many association of service to pseudowire. An entry in this table in instantiated only when LDP signalling is used to configure VPLS service. Each entry in this table provides LDP specific information for the VPlS represented by jnxVplsConfigIndex.')
jnxVplsLdpPwBindMacAddressLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 9, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxVplsLdpPwBindMacAddressLimit.setStatus('current')
if mibBuilder.loadTexts: jnxVplsLdpPwBindMacAddressLimit.setDescription('The value of this object specifies the maximum number of learned and static entries allowed in the Forwarding database for this PW Binding. The value 0 means there is no limit for this PW Binding.')
jnxVplsLdpPwBindMacTableFull = NotificationType((1, 3, 6, 1, 4, 1, 2636, 5, 9, 0, 1)).setObjects(("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"), ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsPwBindIndex"))
if mibBuilder.loadTexts: jnxVplsLdpPwBindMacTableFull.setStatus('current')
if mibBuilder.loadTexts: jnxVplsLdpPwBindMacTableFull.setDescription('The jnxVplsLdpPwBindMacTableFull notification is generated when the number of learned MAC-Addresses increases to the value specified in jnxVplsLdpPwBindMacAddressLimit.')
mibBuilder.exportSymbols("VPLS-LDP-DRAFT-01-MIB", jnxVplsLdpDraft01MIB=jnxVplsLdpDraft01MIB, jnxVplsLdpNotifications=jnxVplsLdpNotifications, jnxVplsLdpConfigEntry=jnxVplsLdpConfigEntry, jnxVplsLdpPwBindMacAddressLimit=jnxVplsLdpPwBindMacAddressLimit, jnxVplsLdpConfigTable=jnxVplsLdpConfigTable, jnxVplsLdpConfigMacAddrWithdraw=jnxVplsLdpConfigMacAddrWithdraw, jnxVplsLdpObjects=jnxVplsLdpObjects, jnxVplsLdpPwBindMacTableFull=jnxVplsLdpPwBindMacTableFull, jnxVplsLdpConformance=jnxVplsLdpConformance, jnxVplsLdpPwBindEntry=jnxVplsLdpPwBindEntry, jnxVplsLdpPwBindTable=jnxVplsLdpPwBindTable, PYSNMP_MODULE_ID=jnxVplsLdpDraft01MIB)
