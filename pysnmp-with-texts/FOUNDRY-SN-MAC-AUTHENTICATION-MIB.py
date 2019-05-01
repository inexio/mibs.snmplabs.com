#
# PySNMP MIB module FOUNDRY-SN-MAC-AUTHENTICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-SN-MAC-AUTHENTICATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:15:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, ObjectIdentity, IpAddress, NotificationType, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Integer32, iso, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "ObjectIdentity", "IpAddress", "NotificationType", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Integer32", "iso", "TimeTicks", "Counter64")
TextualConvention, MacAddress, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "TimeStamp", "DisplayString")
snMacAuth = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28))
snMacAuth.setRevisions(('2010-06-02 00:00', '2007-06-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snMacAuth.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', '',))
if mibBuilder.loadTexts: snMacAuth.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: snMacAuth.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: snMacAuth.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: snMacAuth.setDescription("Management Information Base module for MAC authentication configuration and statistics. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
snMacAuthGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1))
snMacAuthClearGlobalCmd = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthClearGlobalCmd.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearGlobalCmd.setDescription('valid(0) - a SNMP-GET of this mib shows that it is valid command to use. clear(1) - represents clear MAC Authentication table for all ports.')
snMacAuthGlobalConfigState = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthGlobalConfigState.setStatus('current')
if mibBuilder.loadTexts: snMacAuthGlobalConfigState.setDescription('Enable/disable MAC authentication on the global level.')
snMacAuthClearIfCmdTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2), )
if mibBuilder.loadTexts: snMacAuthClearIfCmdTable.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearIfCmdTable.setDescription('The status of clearing an MAC Authentication entry for an interface.')
snMacAuthClearIfCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearIfCmdIfIndex"))
if mibBuilder.loadTexts: snMacAuthClearIfCmdEntry.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearIfCmdEntry.setDescription('An entry of clearing an MAC Authentication entry for an interface.')
snMacAuthClearIfCmdIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacAuthClearIfCmdIfIndex.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearIfCmdIfIndex.setDescription('ifIndex value of the local interface on which a clear command is issued and monitored.')
snMacAuthClearIfCmdAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthClearIfCmdAction.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearIfCmdAction.setDescription('valid(0) - a SNMP-GET of this mib shows that it is valid command to use. clear(1) - represents clearing an MAC Authentication entry for an interface.')
snMacAuthTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3), )
if mibBuilder.loadTexts: snMacAuthTable.setStatus('current')
if mibBuilder.loadTexts: snMacAuthTable.setDescription('MAC Authentication table.')
snMacAuthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthIfIndex"), (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthVlanId"), (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthMac"))
if mibBuilder.loadTexts: snMacAuthEntry.setStatus('current')
if mibBuilder.loadTexts: snMacAuthEntry.setDescription('An entry in the MAC Authentication table.')
snMacAuthIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacAuthIfIndex.setStatus('current')
if mibBuilder.loadTexts: snMacAuthIfIndex.setDescription('In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 2863.')
snMacAuthVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: snMacAuthVlanId.setStatus('current')
if mibBuilder.loadTexts: snMacAuthVlanId.setDescription('The ID of a VLAN of which this port is a member. Port must be untagged. For tagged port which belongs to multiple VLANs, this object return 0 which is an invalid VLAN ID value.')
snMacAuthMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 3), MacAddress())
if mibBuilder.loadTexts: snMacAuthMac.setStatus('current')
if mibBuilder.loadTexts: snMacAuthMac.setDescription('MAC Address to be authenticated.')
snMacAuthState = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authenticate", 1), ("unauthenticate", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthState.setStatus('current')
if mibBuilder.loadTexts: snMacAuthState.setDescription('.')
snMacAuthTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthTimeStamp.setStatus('current')
if mibBuilder.loadTexts: snMacAuthTimeStamp.setDescription('Timestamp at which the MAC was authenticated or failed to be authenticated.')
snMacAuthAge = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthAge.setStatus('current')
if mibBuilder.loadTexts: snMacAuthAge.setDescription('Age of the mac session in which the MAC address is authenticated.')
snMacAuthDot1x = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snMacAuthDot1x.setStatus('current')
if mibBuilder.loadTexts: snMacAuthDot1x.setDescription('Indicates whether the Dot1x is enabled or not.')
snMacAuthClearMacSessionTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4), )
if mibBuilder.loadTexts: snMacAuthClearMacSessionTable.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearMacSessionTable.setDescription('The status of clearing an MAC Session entry indexed by a MAC address.')
snMacAuthClearMacSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1), ).setIndexNames((0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearMacSessionIfIndex"), (0, "FOUNDRY-SN-MAC-AUTHENTICATION-MIB", "snMacAuthClearMacSessionMac"))
if mibBuilder.loadTexts: snMacAuthClearMacSessionEntry.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearMacSessionEntry.setDescription('An entry of clearing an MAC Session entry indexed by a MAC address.')
snMacAuthClearMacSessionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: snMacAuthClearMacSessionIfIndex.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearMacSessionIfIndex.setDescription('ifIndex value of the local interface on which a clear command is issued and monitored.')
snMacAuthClearMacSessionMac = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 2), MacAddress())
if mibBuilder.loadTexts: snMacAuthClearMacSessionMac.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearMacSessionMac.setDescription('An MAC Session entry indexed by a MAC address.')
snMacAuthClearMacSessionAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 28, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("valid", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snMacAuthClearMacSessionAction.setStatus('current')
if mibBuilder.loadTexts: snMacAuthClearMacSessionAction.setDescription('valid(0) - a SNMP-GET of this mib shows that it is valid command to use. clear(1) - represents clearing an MAC Session entry indexed by a MAC address.')
mibBuilder.exportSymbols("FOUNDRY-SN-MAC-AUTHENTICATION-MIB", snMacAuthGlobalConfigState=snMacAuthGlobalConfigState, snMacAuthDot1x=snMacAuthDot1x, snMacAuthEntry=snMacAuthEntry, snMacAuth=snMacAuth, snMacAuthClearIfCmdTable=snMacAuthClearIfCmdTable, snMacAuthVlanId=snMacAuthVlanId, snMacAuthClearMacSessionEntry=snMacAuthClearMacSessionEntry, snMacAuthState=snMacAuthState, snMacAuthClearMacSessionIfIndex=snMacAuthClearMacSessionIfIndex, snMacAuthClearMacSessionMac=snMacAuthClearMacSessionMac, snMacAuthClearMacSessionAction=snMacAuthClearMacSessionAction, snMacAuthTable=snMacAuthTable, snMacAuthClearIfCmdAction=snMacAuthClearIfCmdAction, snMacAuthGlobal=snMacAuthGlobal, PYSNMP_MODULE_ID=snMacAuth, snMacAuthClearIfCmdEntry=snMacAuthClearIfCmdEntry, snMacAuthClearIfCmdIfIndex=snMacAuthClearIfCmdIfIndex, snMacAuthAge=snMacAuthAge, snMacAuthClearMacSessionTable=snMacAuthClearMacSessionTable, snMacAuthMac=snMacAuthMac, snMacAuthIfIndex=snMacAuthIfIndex, snMacAuthClearGlobalCmd=snMacAuthClearGlobalCmd, snMacAuthTimeStamp=snMacAuthTimeStamp)
