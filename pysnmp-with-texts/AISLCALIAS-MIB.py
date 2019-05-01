#
# PySNMP MIB module AISLCALIAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AISLCALIAS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:16:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, TimeTicks, iso, IpAddress, enterprises, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Integer32, Counter32, ObjectIdentity, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "iso", "IpAddress", "enterprises", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Integer32", "Counter32", "ObjectIdentity", "MibIdentifier", "Unsigned32")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSLCAlias = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 22))
if mibBuilder.loadTexts: aiSLCAlias.setLastUpdated('9909141600Z')
if mibBuilder.loadTexts: aiSLCAlias.setOrganization('Applied Innovation Inc.')
if mibBuilder.loadTexts: aiSLCAlias.setContactInfo('Engineering MIB Administrator Postal: Applied Innovation Inc. 5800 Innovation Drive Dublin, Ohio 43017-3271 Tel: 614-798-2000 Fax: 614-798-1770 Email: snmp@aiinet.com')
if mibBuilder.loadTexts: aiSLCAlias.setDescription('MIB module for SLCs with alias translation ability.')
aiSLCAliasTable = MibTable((1, 3, 6, 1, 4, 1, 539, 22, 1), )
if mibBuilder.loadTexts: aiSLCAliasTable.setStatus('current')
if mibBuilder.loadTexts: aiSLCAliasTable.setDescription('Table of aliases stored in the SLC, indexed by alias name. Rows are managed with the SNMPv2 RowStatus mechanism. All strings in this table may be up to 300 characters long, except the description, which may be up to 80.')
aiSLCAliasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 22, 1, 1), ).setIndexNames((1, "AISLCALIAS-MIB", "aislcaliAliasName"))
if mibBuilder.loadTexts: aiSLCAliasEntry.setStatus('current')
if mibBuilder.loadTexts: aiSLCAliasEntry.setDescription('Entry of aiSLCAliasTable.')
aislcaliAliasName = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aislcaliAliasName.setStatus('current')
if mibBuilder.loadTexts: aislcaliAliasName.setDescription('Name of the alias to which this table row applies. Maximum length is 255 characters.')
aislcaliRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 2), RowStatus().clone('active')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliRowStatus.setStatus('current')
if mibBuilder.loadTexts: aislcaliRowStatus.setDescription('Status of this row, as defined by SNMPv2.')
aislcaliDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliDescription.setStatus('current')
if mibBuilder.loadTexts: aislcaliDescription.setDescription('Textual description of this alias. Maximum length is 80 characters.')
aislcaliDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliDestination.setStatus('current')
if mibBuilder.loadTexts: aislcaliDestination.setDescription('Destination of this alias. Maximum length is 255 characters.')
aislcaliShowInDestMenu = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliShowInDestMenu.setStatus('current')
if mibBuilder.loadTexts: aislcaliShowInDestMenu.setDescription('Show this alias in the destination menu.')
aislcaliCallingAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliCallingAddr.setStatus('current')
if mibBuilder.loadTexts: aislcaliCallingAddr.setDescription('Address of the entity calling this alias. Maximum length is 255 characters.')
aislcaliCalledAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliCalledAddr.setStatus('current')
if mibBuilder.loadTexts: aislcaliCalledAddr.setDescription('Address called by this alias. Maximum length is 255 characters.')
aislcaliCallData = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliCallData.setStatus('current')
if mibBuilder.loadTexts: aislcaliCallData.setDescription('String used for SLC-dependent features. Maximum length is 255 characters.')
aislcaliCallingProto = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 9), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliCallingProto.setStatus('current')
if mibBuilder.loadTexts: aislcaliCallingProto.setDescription('Protocol used by the entity calling this alias. Maximum length is 255 characters.')
aislcaliCalledProto = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 10), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliCalledProto.setStatus('current')
if mibBuilder.loadTexts: aislcaliCalledProto.setDescription('Protocol used for a call placed by this alias. Maximum length is 255 characters.')
aislcaliAppString = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 11), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliAppString.setStatus('current')
if mibBuilder.loadTexts: aislcaliAppString.setDescription('String used for SLC-dependent features. Maximum length is 255 characters.')
aislcaliAltRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 22, 1, 1, 12), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aislcaliAltRoute.setStatus('current')
if mibBuilder.loadTexts: aislcaliAltRoute.setDescription('Name of an alternative alias the SLC can use. Maximum length is 255 characters.')
mibBuilder.exportSymbols("AISLCALIAS-MIB", aiSLCAliasEntry=aiSLCAliasEntry, aii=aii, aislcaliCallData=aislcaliCallData, aiSLCAliasTable=aiSLCAliasTable, aislcaliAltRoute=aislcaliAltRoute, aiSLCAlias=aiSLCAlias, aislcaliCalledProto=aislcaliCalledProto, aislcaliDescription=aislcaliDescription, aislcaliShowInDestMenu=aislcaliShowInDestMenu, aislcaliAppString=aislcaliAppString, PYSNMP_MODULE_ID=aiSLCAlias, aislcaliRowStatus=aislcaliRowStatus, aislcaliCallingAddr=aislcaliCallingAddr, aislcaliDestination=aislcaliDestination, aislcaliCalledAddr=aislcaliCalledAddr, aislcaliAliasName=aislcaliAliasName, aislcaliCallingProto=aislcaliCallingProto)
