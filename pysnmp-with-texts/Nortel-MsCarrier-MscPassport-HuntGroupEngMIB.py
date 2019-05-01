#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-HuntGroupEngMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-HuntGroupEngMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:30:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
mscLpEngIndex, mscLpEng, mscLpIndex = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex", "mscLpEng", "mscLpIndex")
Unsigned32, Counter32, RowStatus, DisplayString, StorageType = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "Unsigned32", "Counter32", "RowStatus", "DisplayString", "StorageType")
NonReplicated, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "NonReplicated")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, Counter32, Gauge32, Unsigned32, iso, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, IpAddress, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Counter32", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "IpAddress", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
huntGroupEngMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131))
mscLpEngHgs = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4))
mscLpEngHgsRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1), )
if mibBuilder.loadTexts: mscLpEngHgsRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscLpEngHgsRowStatusTable.setDescription('This entry controls the addition and deletion of mscLpEngHgs components.')
mscLpEngHgsRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"), (0, "Nortel-MsCarrier-MscPassport-HuntGroupEngMIB", "mscLpEngHgsIndex"))
if mibBuilder.loadTexts: mscLpEngHgsRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscLpEngHgsRowStatusEntry.setDescription('A single entry in the table represents a single mscLpEngHgs component.')
mscLpEngHgsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscLpEngHgsRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscLpEngHgsRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscLpEngHgs components. These components can be added and deleted.')
mscLpEngHgsComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpEngHgsComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscLpEngHgsComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscLpEngHgsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpEngHgsStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscLpEngHgsStorageType.setDescription('This variable represents the storage type value for the mscLpEngHgs tables.')
mscLpEngHgsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscLpEngHgsIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscLpEngHgsIndex.setDescription('This variable represents the index for the mscLpEngHgs tables.')
mscLpEngHgsOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 10), )
if mibBuilder.loadTexts: mscLpEngHgsOperationalTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscLpEngHgsOperationalTable.setDescription('The Operational group contains attributes for all hunt groups on the LP.')
mscLpEngHgsOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"), (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpEngIndex"), (0, "Nortel-MsCarrier-MscPassport-HuntGroupEngMIB", "mscLpEngHgsIndex"))
if mibBuilder.loadTexts: mscLpEngHgsOperationalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscLpEngHgsOperationalEntry.setDescription('An entry in the mscLpEngHgsOperationalTable.')
mscLpEngHgsHuntGroups = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpEngHgsHuntGroups.setStatus('mandatory')
if mibBuilder.loadTexts: mscLpEngHgsHuntGroups.setDescription('This attribute indicates the number of hunt groups provisioned on the LP.')
mscLpEngHgsHuntAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 23, 4, 10, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscLpEngHgsHuntAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: mscLpEngHgsHuntAttempts.setDescription('This attribute counts the total number of hunt attempts made by all hunt groups. The count includes both initial and subsequent hunt attempts. Individual hunt groups maintain this counter within the huntAttempts attribute of the Hg/n component. This counter wraps to 0 when it exceeds its maximum value.')
huntGroupEngGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 1))
huntGroupEngGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 1, 1))
huntGroupEngGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 1, 1, 3))
huntGroupEngGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 1, 1, 3, 2))
huntGroupEngCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 3))
huntGroupEngCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 3, 1))
huntGroupEngCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 3, 1, 3))
huntGroupEngCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 131, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-HuntGroupEngMIB", huntGroupEngCapabilitiesCA=huntGroupEngCapabilitiesCA, huntGroupEngGroupCA=huntGroupEngGroupCA, mscLpEngHgsRowStatusTable=mscLpEngHgsRowStatusTable, mscLpEngHgsRowStatusEntry=mscLpEngHgsRowStatusEntry, mscLpEngHgsIndex=mscLpEngHgsIndex, mscLpEngHgsOperationalTable=mscLpEngHgsOperationalTable, huntGroupEngMIB=huntGroupEngMIB, mscLpEngHgsStorageType=mscLpEngHgsStorageType, huntGroupEngCapabilitiesCA02=huntGroupEngCapabilitiesCA02, mscLpEngHgsHuntGroups=mscLpEngHgsHuntGroups, huntGroupEngGroupCA02=huntGroupEngGroupCA02, mscLpEngHgs=mscLpEngHgs, huntGroupEngCapabilities=huntGroupEngCapabilities, mscLpEngHgsHuntAttempts=mscLpEngHgsHuntAttempts, mscLpEngHgsComponentName=mscLpEngHgsComponentName, huntGroupEngGroup=huntGroupEngGroup, huntGroupEngCapabilitiesCA02A=huntGroupEngCapabilitiesCA02A, mscLpEngHgsRowStatus=mscLpEngHgsRowStatus, mscLpEngHgsOperationalEntry=mscLpEngHgsOperationalEntry, huntGroupEngGroupCA02A=huntGroupEngGroupCA02A)
