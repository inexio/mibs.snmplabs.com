#
# PySNMP MIB module RFC1318-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1318-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:56:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, transmission, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, IpAddress, ModuleIdentity, Counter32, Counter64, MibIdentifier, Unsigned32, Integer32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "transmission", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "IpAddress", "ModuleIdentity", "Counter32", "Counter64", "MibIdentifier", "Unsigned32", "Integer32", "NotificationType", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
para = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 34))
paraNumber = MibScalar((1, 3, 6, 1, 2, 1, 10, 34, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraNumber.setStatus('mandatory')
if mibBuilder.loadTexts: paraNumber.setDescription('The number of ports (regardless of their current state) in the Parallel-printer-like port table.')
paraPortTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 2), )
if mibBuilder.loadTexts: paraPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: paraPortTable.setDescription('A list of port entries. The number of entries is given by the value of paraNumber.')
paraPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 2, 1), ).setIndexNames((0, "RFC1318-MIB", "paraPortIndex"))
if mibBuilder.loadTexts: paraPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: paraPortEntry.setDescription('Status and parameter values for a port.')
paraPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: paraPortIndex.setDescription('A unique value for each port. Its value ranges between 1 and the value of paraNumber. By convention and if possible, hardware port numbers map directly to external connectors. The value for each port must remain constant at least from one re-initialization of the network management agent to the next.')
paraPortType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("centronics", 2), ("dataproducts", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortType.setStatus('mandatory')
if mibBuilder.loadTexts: paraPortType.setDescription("The port's hardware type.")
paraPortInSigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortInSigNumber.setStatus('mandatory')
if mibBuilder.loadTexts: paraPortInSigNumber.setDescription('The number of input signals for the port in the input signal table (paraPortInSigTable). The table contains entries only for those signals the software can detect.')
paraPortOutSigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraPortOutSigNumber.setStatus('mandatory')
if mibBuilder.loadTexts: paraPortOutSigNumber.setDescription('The number of output signals for the port in the output signal table (paraPortOutSigTable). The table contains entries only for those signals the software can assert.')
paraInSigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 3), )
if mibBuilder.loadTexts: paraInSigTable.setStatus('mandatory')
if mibBuilder.loadTexts: paraInSigTable.setDescription('A list of port input control signal entries.')
paraInSigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 3, 1), ).setIndexNames((0, "RFC1318-MIB", "paraInSigPortIndex"), (0, "RFC1318-MIB", "paraInSigName"))
if mibBuilder.loadTexts: paraInSigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: paraInSigEntry.setDescription('Input control signal status for a hardware port.')
paraInSigPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: paraInSigPortIndex.setDescription('The value of paraPortIndex for the port to which this entry belongs.')
paraInSigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("power", 1), ("online", 2), ("busy", 3), ("paperout", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigName.setStatus('mandatory')
if mibBuilder.loadTexts: paraInSigName.setDescription('Identification of a hardware signal.')
paraInSigState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigState.setStatus('mandatory')
if mibBuilder.loadTexts: paraInSigState.setDescription('The current signal state.')
paraInSigChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraInSigChanges.setStatus('mandatory')
if mibBuilder.loadTexts: paraInSigChanges.setDescription("The number of times the signal has changed from 'on' to 'off' or from 'off' to 'on'.")
paraOutSigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 34, 4), )
if mibBuilder.loadTexts: paraOutSigTable.setStatus('mandatory')
if mibBuilder.loadTexts: paraOutSigTable.setDescription('A list of port output control signal entries.')
paraOutSigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 34, 4, 1), ).setIndexNames((0, "RFC1318-MIB", "paraOutSigPortIndex"), (0, "RFC1318-MIB", "paraOutSigName"))
if mibBuilder.loadTexts: paraOutSigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: paraOutSigEntry.setDescription('Output control signal status for a hardware port.')
paraOutSigPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: paraOutSigPortIndex.setDescription('The value of paraPortIndex for the port to which this entry belongs.')
paraOutSigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("power", 1), ("online", 2), ("busy", 3), ("paperout", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigName.setStatus('mandatory')
if mibBuilder.loadTexts: paraOutSigName.setDescription('Identification of a hardware signal.')
paraOutSigState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigState.setStatus('mandatory')
if mibBuilder.loadTexts: paraOutSigState.setDescription('The current signal state.')
paraOutSigChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 34, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: paraOutSigChanges.setStatus('mandatory')
if mibBuilder.loadTexts: paraOutSigChanges.setDescription("The number of times the signal has changed from 'on' to 'off' or from 'off' to 'on'.")
mibBuilder.exportSymbols("RFC1318-MIB", paraOutSigPortIndex=paraOutSigPortIndex, paraPortTable=paraPortTable, paraPortEntry=paraPortEntry, paraOutSigState=paraOutSigState, paraInSigPortIndex=paraInSigPortIndex, paraOutSigTable=paraOutSigTable, paraOutSigName=paraOutSigName, paraPortInSigNumber=paraPortInSigNumber, paraInSigName=paraInSigName, paraOutSigChanges=paraOutSigChanges, paraPortIndex=paraPortIndex, paraPortType=paraPortType, paraInSigEntry=paraInSigEntry, paraInSigState=paraInSigState, paraNumber=paraNumber, paraPortOutSigNumber=paraPortOutSigNumber, paraInSigTable=paraInSigTable, paraOutSigEntry=paraOutSigEntry, para=para, paraInSigChanges=paraInSigChanges)
