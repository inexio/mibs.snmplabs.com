#
# PySNMP MIB module JUNIPER-LSYSSPAUTHENTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-LSYSSPAUTHENTRY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
jnxLsysSpAuthentry, = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpAuthentry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, IpAddress, NotificationType, TimeTicks, Bits, Counter32, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "IpAddress", "NotificationType", "TimeTicks", "Bits", "Counter32", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxLsysSpAuthentryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1))
if mibBuilder.loadTexts: jnxLsysSpAuthentryMIB.setLastUpdated('201005191644Z')
if mibBuilder.loadTexts: jnxLsysSpAuthentryMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxLsysSpAuthentryMIB.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: jnxLsysSpAuthentryMIB.setDescription('This module defines the auth-entry-specific MIB for Juniper Enterprise Logical-System (LSYS) security profiles. Juniper documentation is recommended as the reference. The LSYS security profile provides various static and dynamic resource management by observing resource quota limits. Security auth-entry resource is the focus in this MIB. ')
jnxLsysSpAuthentryObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1))
jnxLsysSpAuthentrySummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2))
jnxLsysSpAuthentryTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1), )
if mibBuilder.loadTexts: jnxLsysSpAuthentryTable.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryTable.setDescription('LSYSPROFILE auth-entry objects for auth-entry resource consumption per LSYS.')
jnxLsysSpAuthentryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1), ).setIndexNames((1, "JUNIPER-LSYSSPAUTHENTRY-MIB", "jnxLsysSpAuthentryLsysName"))
if mibBuilder.loadTexts: jnxLsysSpAuthentryEntry.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryEntry.setDescription('An entry in auth-entry resource table.')
jnxLsysSpAuthentryLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: jnxLsysSpAuthentryLsysName.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryLsysName.setDescription('The name of the logical system for which auth-entry resource information is retrieved. ')
jnxLsysSpAuthentryProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryProfileName.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryProfileName.setDescription('The security profile name string for the LSYS.')
jnxLsysSpAuthentryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryUsage.setDescription('The current resource usage count for the LSYS.')
jnxLsysSpAuthentryReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryReserved.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryReserved.setDescription('The reserved resource count for the LSYS.')
jnxLsysSpAuthentryMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryMaximum.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryMaximum.setDescription('The maximum allowed resource usage count for the LSYS.')
jnxLsysSpAuthentryUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryUsedAmount.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryUsedAmount.setDescription('The auth-entry resource consumption over all LSYS.')
jnxLsysSpAuthentryMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryMaxQuota.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryMaxQuota.setDescription('The auth-entry resource maximum quota for the whole device for all LSYS.')
jnxLsysSpAuthentryAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryAvailableAmount.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryAvailableAmount.setDescription('The auth-entry resource available in the whole device.')
jnxLsysSpAuthentryHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryHeaviestUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryHeaviestUsage.setDescription('The most amount of auth-entry resource consumed of a LSYS.')
jnxLsysSpAuthentryHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryHeaviestUser.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryHeaviestUser.setDescription('The LSYS name that consume the most auth-entry resource.')
jnxLsysSpAuthentryLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryLightestUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryLightestUsage.setDescription('The least amount of auth-entry resource consumed of a LSYS.')
jnxLsysSpAuthentryLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 7, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpAuthentryLightestUser.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpAuthentryLightestUser.setDescription('The LSYS name that consume the least auth-entry resource.')
mibBuilder.exportSymbols("JUNIPER-LSYSSPAUTHENTRY-MIB", jnxLsysSpAuthentrySummary=jnxLsysSpAuthentrySummary, jnxLsysSpAuthentryProfileName=jnxLsysSpAuthentryProfileName, jnxLsysSpAuthentryMIB=jnxLsysSpAuthentryMIB, jnxLsysSpAuthentryUsedAmount=jnxLsysSpAuthentryUsedAmount, jnxLsysSpAuthentryUsage=jnxLsysSpAuthentryUsage, jnxLsysSpAuthentryEntry=jnxLsysSpAuthentryEntry, jnxLsysSpAuthentryHeaviestUsage=jnxLsysSpAuthentryHeaviestUsage, jnxLsysSpAuthentryLsysName=jnxLsysSpAuthentryLsysName, jnxLsysSpAuthentryLightestUsage=jnxLsysSpAuthentryLightestUsage, jnxLsysSpAuthentryTable=jnxLsysSpAuthentryTable, jnxLsysSpAuthentryReserved=jnxLsysSpAuthentryReserved, PYSNMP_MODULE_ID=jnxLsysSpAuthentryMIB, jnxLsysSpAuthentryObjects=jnxLsysSpAuthentryObjects, jnxLsysSpAuthentryMaxQuota=jnxLsysSpAuthentryMaxQuota, jnxLsysSpAuthentryMaximum=jnxLsysSpAuthentryMaximum, jnxLsysSpAuthentryHeaviestUser=jnxLsysSpAuthentryHeaviestUser, jnxLsysSpAuthentryLightestUser=jnxLsysSpAuthentryLightestUser, jnxLsysSpAuthentryAvailableAmount=jnxLsysSpAuthentryAvailableAmount)
