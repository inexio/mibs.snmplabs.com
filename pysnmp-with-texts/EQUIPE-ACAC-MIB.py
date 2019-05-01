#
# PySNMP MIB module EQUIPE-ACAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EQUIPE-ACAC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:05:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
AtmServiceCategory, = mibBuilder.importSymbols("ATM-TC-MIB", "AtmServiceCategory")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, enterprises, NotificationType, MibIdentifier, Unsigned32, ModuleIdentity, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Counter64, ObjectIdentity, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "NotificationType", "MibIdentifier", "Unsigned32", "ModuleIdentity", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Counter64", "ObjectIdentity", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
equipe = MibIdentifier((1, 3, 6, 1, 4, 1, 5022))
eqAcacMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5022, 5))
if mibBuilder.loadTexts: eqAcacMib.setLastUpdated('0012270000Z')
if mibBuilder.loadTexts: eqAcacMib.setOrganization('')
if mibBuilder.loadTexts: eqAcacMib.setContactInfo('Jas Parmar Equipe Communications 100 Nagog Park Acton MA 01720')
if mibBuilder.loadTexts: eqAcacMib.setDescription('This is the Equipe ACAC MIB module.')
eqAcacViTable = MibTable((1, 3, 6, 1, 4, 1, 5022, 5, 1), )
if mibBuilder.loadTexts: eqAcacViTable.setStatus('current')
if mibBuilder.loadTexts: eqAcacViTable.setDescription('This table contains stats for an ACAC logical port.')
eqAcacViEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1), ).setIndexNames((0, "EQUIPE-ACAC-MIB", "eqAcacViIfIndex"))
if mibBuilder.loadTexts: eqAcacViEntry.setStatus('current')
if mibBuilder.loadTexts: eqAcacViEntry.setDescription('An ACAC logical port stats entry.')
eqAcacViIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViIfIndex.setStatus('current')
if mibBuilder.loadTexts: eqAcacViIfIndex.setDescription('The ifIndex for the logical port.')
eqAcacViStartingBw = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViStartingBw.setStatus('current')
if mibBuilder.loadTexts: eqAcacViStartingBw.setDescription('The initial amount of bandwidth allocated to this virtual interface (in cells per second).')
eqAcacViConsumedBw = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViConsumedBw.setStatus('current')
if mibBuilder.loadTexts: eqAcacViConsumedBw.setDescription('The amount of bandwidth consumed by existing circuits (in cells per second).')
eqAcacViInConsideredCcts = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViInConsideredCcts.setStatus('current')
if mibBuilder.loadTexts: eqAcacViInConsideredCcts.setDescription('The number of circuits that CAC has been asked to consider for admission.')
eqAcacViInRejectedCcts = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViInRejectedCcts.setStatus('current')
if mibBuilder.loadTexts: eqAcacViInRejectedCcts.setDescription('The number of circuits that CAC has been asked to consider for admission for which sufficient resources have not been available. Hence the circuit was rejected.')
eqAcacViInActiveCcts = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViInActiveCcts.setStatus('current')
if mibBuilder.loadTexts: eqAcacViInActiveCcts.setDescription('The number of currently active circuits')
eqAcacViInReservedCcts = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViInReservedCcts.setStatus('current')
if mibBuilder.loadTexts: eqAcacViInReservedCcts.setDescription('The number of circuits that CAC has reserved resources, but is waiting for a commit.')
eqAcacViOutConsideredCcts = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViOutConsideredCcts.setStatus('current')
if mibBuilder.loadTexts: eqAcacViOutConsideredCcts.setDescription('The number of circuits that CAC has been asked to consider for admission.')
eqAcacViOutRejectedCcts = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViOutRejectedCcts.setStatus('current')
if mibBuilder.loadTexts: eqAcacViOutRejectedCcts.setDescription('The number of circuits that CAC has been asked to consider for admission for which sufficient resources have not been available. Hence the circuit was rejected.')
eqAcacViOutActiveCcts = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViOutActiveCcts.setStatus('current')
if mibBuilder.loadTexts: eqAcacViOutActiveCcts.setDescription('The number of currently active circuits.')
eqAcacViOutReservedCcts = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViOutReservedCcts.setStatus('current')
if mibBuilder.loadTexts: eqAcacViOutReservedCcts.setDescription('The number of circuits that CAC has reserved resources, but is waiting for a commit.')
eqAcacViServCatTable = MibTable((1, 3, 6, 1, 4, 1, 5022, 5, 2), )
if mibBuilder.loadTexts: eqAcacViServCatTable.setStatus('current')
if mibBuilder.loadTexts: eqAcacViServCatTable.setDescription('This table contains stats per ATM Service Category for an ACAC logical port.')
eqAcacViServCatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5022, 5, 2, 1), ).setIndexNames((0, "EQUIPE-ACAC-MIB", "eqAcacViServCatIfIndex"), (0, "EQUIPE-ACAC-MIB", "eqAcacViServCatServiceCategory"))
if mibBuilder.loadTexts: eqAcacViServCatEntry.setStatus('current')
if mibBuilder.loadTexts: eqAcacViServCatEntry.setDescription('An ACAC logical port service category stats entry.')
eqAcacViServCatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViServCatIfIndex.setStatus('current')
if mibBuilder.loadTexts: eqAcacViServCatIfIndex.setDescription('The ifIndex for the logical port.')
eqAcacViServCatServiceCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 2, 1, 2), AtmServiceCategory()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViServCatServiceCategory.setStatus('current')
if mibBuilder.loadTexts: eqAcacViServCatServiceCategory.setDescription('The Service Category that this instance in the table describes.')
eqAcacViServCatConsumedBw = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViServCatConsumedBw.setStatus('current')
if mibBuilder.loadTexts: eqAcacViServCatConsumedBw.setDescription('The amount of bandwidth currently considered in use by this service category for the purposes of CAC calculations. Note that this does not represent actual traffic utilitization.')
eqAcacViServCatActiveCcts = MibTableColumn((1, 3, 6, 1, 4, 1, 5022, 5, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqAcacViServCatActiveCcts.setStatus('current')
if mibBuilder.loadTexts: eqAcacViServCatActiveCcts.setDescription('The number of active circuits for this service category on this virtual interface.')
mibBuilder.exportSymbols("EQUIPE-ACAC-MIB", eqAcacViEntry=eqAcacViEntry, equipe=equipe, eqAcacViTable=eqAcacViTable, eqAcacViIfIndex=eqAcacViIfIndex, eqAcacViOutConsideredCcts=eqAcacViOutConsideredCcts, eqAcacViServCatEntry=eqAcacViServCatEntry, PYSNMP_MODULE_ID=eqAcacMib, eqAcacViStartingBw=eqAcacViStartingBw, eqAcacViOutActiveCcts=eqAcacViOutActiveCcts, eqAcacViServCatServiceCategory=eqAcacViServCatServiceCategory, eqAcacViInRejectedCcts=eqAcacViInRejectedCcts, eqAcacViServCatActiveCcts=eqAcacViServCatActiveCcts, eqAcacViInConsideredCcts=eqAcacViInConsideredCcts, eqAcacViInActiveCcts=eqAcacViInActiveCcts, eqAcacViOutReservedCcts=eqAcacViOutReservedCcts, eqAcacViConsumedBw=eqAcacViConsumedBw, eqAcacViServCatIfIndex=eqAcacViServCatIfIndex, eqAcacViServCatTable=eqAcacViServCatTable, eqAcacMib=eqAcacMib, eqAcacViOutRejectedCcts=eqAcacViOutRejectedCcts, eqAcacViServCatConsumedBw=eqAcacViServCatConsumedBw, eqAcacViInReservedCcts=eqAcacViInReservedCcts)
