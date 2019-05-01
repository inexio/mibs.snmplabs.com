#
# PySNMP MIB module JUNIPER-LSYSSP-NATSRCPOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-LSYSSP-NATSRCPOOL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
jnxLsysSpNATsrcpool, = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpNATsrcpool")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, MibIdentifier, iso, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, Integer32, IpAddress, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "MibIdentifier", "iso", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "Integer32", "IpAddress", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxLsysSpNATsrcpoolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1))
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolMIB.setLastUpdated('201005191644Z')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolMIB.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolMIB.setDescription('This module defines the NAT-src-pool-specific MIB for Juniper Enterprise Logical-System (LSYS) security profiles. Juniper documentation is recommended as the reference. The LSYS security profile provides various static and dynamic resource management by observing resource quota limits. Security NAT-src-pool resource is the focus in this MIB. ')
jnxLsysSpNATsrcpoolObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1))
jnxLsysSpNATsrcpoolSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2))
jnxLsysSpNATsrcpoolTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1), )
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolTable.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolTable.setDescription('LSYSPROFILE NAT-src-pool objects for NAT-src-pool resource consumption per LSYS.')
jnxLsysSpNATsrcpoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1), ).setIndexNames((1, "JUNIPER-LSYSSP-NATSRCPOOL-MIB", "jnxLsysSpNATsrcpoolLsysName"))
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolEntry.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolEntry.setDescription('An entry in NAT-src-pool resource table.')
jnxLsysSpNATsrcpoolLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolLsysName.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolLsysName.setDescription('The name of the logical system for which NAT-src-pool resource information is retrieved. ')
jnxLsysSpNATsrcpoolProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolProfileName.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolProfileName.setDescription('The security profile name string for the LSYS.')
jnxLsysSpNATsrcpoolUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolUsage.setDescription('The current resource usage count for the LSYS.')
jnxLsysSpNATsrcpoolReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolReserved.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolReserved.setDescription('The reserved resource count for the LSYS.')
jnxLsysSpNATsrcpoolMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolMaximum.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolMaximum.setDescription('The maximum allowed resource usage count for the LSYS.')
jnxLsysSpNATsrcpoolUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolUsedAmount.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolUsedAmount.setDescription('The NAT-src-pool resource consumption over all LSYS.')
jnxLsysSpNATsrcpoolMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolMaxQuota.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolMaxQuota.setDescription('The NAT-src-pool resource maximum quota for the whole device for all LSYS.')
jnxLsysSpNATsrcpoolAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolAvailableAmount.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolAvailableAmount.setDescription('The NAT-src-pool resource available in the whole device.')
jnxLsysSpNATsrcpoolHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolHeaviestUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolHeaviestUsage.setDescription('The most amount of NAT-src-pool resource consumed of a LSYS.')
jnxLsysSpNATsrcpoolHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolHeaviestUser.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolHeaviestUser.setDescription('The LSYS name that consume the most NAT-src-pool resource.')
jnxLsysSpNATsrcpoolLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolLightestUsage.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolLightestUsage.setDescription('The least amount of NAT-src-pool resource consumed of a LSYS.')
jnxLsysSpNATsrcpoolLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 8, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolLightestUser.setStatus('current')
if mibBuilder.loadTexts: jnxLsysSpNATsrcpoolLightestUser.setDescription('The LSYS name that consume the least NAT-src-pool resource.')
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATSRCPOOL-MIB", jnxLsysSpNATsrcpoolHeaviestUser=jnxLsysSpNATsrcpoolHeaviestUser, jnxLsysSpNATsrcpoolProfileName=jnxLsysSpNATsrcpoolProfileName, jnxLsysSpNATsrcpoolAvailableAmount=jnxLsysSpNATsrcpoolAvailableAmount, jnxLsysSpNATsrcpoolEntry=jnxLsysSpNATsrcpoolEntry, jnxLsysSpNATsrcpoolLsysName=jnxLsysSpNATsrcpoolLsysName, PYSNMP_MODULE_ID=jnxLsysSpNATsrcpoolMIB, jnxLsysSpNATsrcpoolReserved=jnxLsysSpNATsrcpoolReserved, jnxLsysSpNATsrcpoolLightestUsage=jnxLsysSpNATsrcpoolLightestUsage, jnxLsysSpNATsrcpoolLightestUser=jnxLsysSpNATsrcpoolLightestUser, jnxLsysSpNATsrcpoolMIB=jnxLsysSpNATsrcpoolMIB, jnxLsysSpNATsrcpoolHeaviestUsage=jnxLsysSpNATsrcpoolHeaviestUsage, jnxLsysSpNATsrcpoolTable=jnxLsysSpNATsrcpoolTable, jnxLsysSpNATsrcpoolObjects=jnxLsysSpNATsrcpoolObjects, jnxLsysSpNATsrcpoolMaximum=jnxLsysSpNATsrcpoolMaximum, jnxLsysSpNATsrcpoolMaxQuota=jnxLsysSpNATsrcpoolMaxQuota, jnxLsysSpNATsrcpoolSummary=jnxLsysSpNATsrcpoolSummary, jnxLsysSpNATsrcpoolUsedAmount=jnxLsysSpNATsrcpoolUsedAmount, jnxLsysSpNATsrcpoolUsage=jnxLsysSpNATsrcpoolUsage)
