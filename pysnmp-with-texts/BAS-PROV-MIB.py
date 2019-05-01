#
# PySNMP MIB module BAS-PROV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-PROV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:34:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
basProvInfo, = mibBuilder.importSymbols("BAS-MIB", "basProvInfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, TimeTicks, Counter64, IpAddress, Gauge32, ObjectIdentity, NotificationType, Counter32, Unsigned32, Bits, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "TimeTicks", "Counter64", "IpAddress", "Gauge32", "ObjectIdentity", "NotificationType", "Counter32", "Unsigned32", "Bits", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
basProvInfoMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1))
if mibBuilder.loadTexts: basProvInfoMib.setLastUpdated('9901180900Z')
if mibBuilder.loadTexts: basProvInfoMib.setOrganization('Broadband Access Systems')
if mibBuilder.loadTexts: basProvInfoMib.setContactInfo(' Tech Support Broadband Access Systems 201 Forest Street Marlboro, MA 01752 U.S.A. 508-485-8200 support@basystems.com')
if mibBuilder.loadTexts: basProvInfoMib.setDescription('This MIB module defines the Provisioning Mib for a Broadband Access System Chassis.')
basProvObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1))
basProvServerId = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basProvServerId.setStatus('current')
if mibBuilder.loadTexts: basProvServerId.setDescription('The Provisioning Server unique Id')
basProvInfoLdapServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basProvInfoLdapServerIpAddr.setStatus('current')
if mibBuilder.loadTexts: basProvInfoLdapServerIpAddr.setDescription('The LDAP Server IP Address to access the provisioning server database')
basProvInfoLdapServerPort = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basProvInfoLdapServerPort.setStatus('current')
if mibBuilder.loadTexts: basProvInfoLdapServerPort.setDescription('The LDAP Server Port to access the provisioning server database')
basProvInfoLdapServerUserName = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basProvInfoLdapServerUserName.setStatus('current')
if mibBuilder.loadTexts: basProvInfoLdapServerUserName.setDescription('The LDAP Server username to access the provisioning server database')
basProvInfoLdapServerPassword = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basProvInfoLdapServerPassword.setStatus('current')
if mibBuilder.loadTexts: basProvInfoLdapServerPassword.setDescription('The LDAP Server Password to access the provisioning server database')
mibBuilder.exportSymbols("BAS-PROV-MIB", basProvInfoLdapServerPort=basProvInfoLdapServerPort, basProvInfoLdapServerIpAddr=basProvInfoLdapServerIpAddr, PYSNMP_MODULE_ID=basProvInfoMib, basProvInfoLdapServerPassword=basProvInfoLdapServerPassword, basProvInfoMib=basProvInfoMib, basProvObjects=basProvObjects, basProvInfoLdapServerUserName=basProvInfoLdapServerUserName, basProvServerId=basProvServerId)
