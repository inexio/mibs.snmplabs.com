#
# PySNMP MIB module SUN-SEA-PROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUN-SEA-PROXY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:12:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, Counter64, Gauge32, Bits, Integer32, ObjectIdentity, iso, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "Counter64", "Gauge32", "Bits", "Integer32", "ObjectIdentity", "iso", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
products, = mibBuilder.importSymbols("SUN-MIB", "products")
sunSeaProxyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 15))
if mibBuilder.loadTexts: sunSeaProxyMIB.setLastUpdated('200309180000Z')
if mibBuilder.loadTexts: sunSeaProxyMIB.setOrganization('Sun Microsystems, Inc.')
if mibBuilder.loadTexts: sunSeaProxyMIB.setContactInfo('Customer support')
if mibBuilder.loadTexts: sunSeaProxyMIB.setDescription('The MIB used to manage the snmpdx master agent daemon ')
sunSeaProxyMIBStatusFile = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 15, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSeaProxyMIBStatusFile.setStatus('mandatory')
if mibBuilder.loadTexts: sunSeaProxyMIBStatusFile.setDescription("This file stores the process id's of all the sub agents that are invoked by the master agent. The purpose of this file is for Master Agent recovery in case the Master Agent dies or is killed. When the Master Agent restarts, the entries in this file will indicate which subagents are spawned by it previously and what were their port numbers.")
sunSeaProxyMIBResourceConfigFile = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 15, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSeaProxyMIBResourceConfigFile.setStatus('mandatory')
if mibBuilder.loadTexts: sunSeaProxyMIBResourceConfigFile.setDescription('This file is exclusively used by the Master Agent. When the Master Agent comes up, it reads this file. This files stores information for all those agents that can be managed by the Master Agent. Each entry in the configuration file also includes the methods for invoking these subagents. It is also possible for a subagent not to have an entry in this configuration file. Such a subagent can dynamically come up and register with the Master Agent when it comes up.')
sunSeaProxyMIBConfigurationDir = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 15, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSeaProxyMIBConfigurationDir.setStatus('mandatory')
if mibBuilder.loadTexts: sunSeaProxyMIBConfigurationDir.setDescription('This is the directory that contains the configuration files for the Master Agent.')
sunSeaProxyMIBTrapPort = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 15, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSeaProxyMIBTrapPort.setStatus('mandatory')
if mibBuilder.loadTexts: sunSeaProxyMIBTrapPort.setDescription('This is the port that master agent opens to receive SNMP trap notifications from various subagents. The master agent forwards these traps to the managers appropriately.')
sunCheckSubAgentName = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 15, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunCheckSubAgentName.setStatus('mandatory')
if mibBuilder.loadTexts: sunCheckSubAgentName.setDescription('This variable is of use to the sub agents only. It is used by the sub agents to check with the master to check for duplicate sub agent names.')
sunSeaProxyMIBPollInterval = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 15, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSeaProxyMIBPollInterval.setStatus('mandatory')
if mibBuilder.loadTexts: sunSeaProxyMIBPollInterval.setDescription('This variable speicifies the time interval after which the Master Agent will perform activities other than receiving/sending of SNMP messages. The other activities include trying to find out if there is a change in the resource file, discover if all the agents are responding, and other such routine house keeping activities. This field contains values in seconds.')
sunSeaProxyMIBMaxAgentTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 15, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSeaProxyMIBMaxAgentTimeOut.setStatus('mandatory')
if mibBuilder.loadTexts: sunSeaProxyMIBMaxAgentTimeOut.setDescription('The value of this field can be specified in microseconds. This field signifies the max allowed time-out a subagent can request during registration; e.g., when the Master Agent sends a request to a subagent. It waits for some time-out to receive the response. This time-out can be specified in the registration file or can also be set using dynamic registration. If an agent sets this time-out outrageously high, it can create problems for the Master Agent and other agents. To avoid such a problem, the Master Agent can have a policy of specifying a maximum value for which the Master Agent will wait for a response from the subagent. This maximum value of time-out is specified with this variable.')
sunSubAgentTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 15, 8), )
if mibBuilder.loadTexts: sunSubAgentTable.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentTable.setDescription("This table lists all the sub-agents that are registered with the master agent. The list contains the names of all the sub agents that are currently running on the system. Some of these sub agents could be invoked by the master agent and other's could have benn invoked by other means.")
sunSubAgentTableIndex = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 15, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentTableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentTableIndex.setDescription('The next available index in sunSubAgentTable.')
sunSubAgentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1), ).setIndexNames((0, "SUN-SEA-PROXY-MIB", "sunSubAgentID"))
if mibBuilder.loadTexts: sunSubAgentEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentEntry.setDescription('An entry in the sub-agent table.')
sunSubAgentID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSubAgentID.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentID.setDescription('This is the id for each sub agent that is running and registered with the master agent.')
sunSubAgentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("init", 1), ("load", 2), ("active", 3), ("inactive", 4), ("destroy", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentStatus.setDescription("This variable provides the state of the sub-agent. When the sub-agent is started the state is 'init'. Once the sub-agent has read it's configuration files, but has not registered with the master , the state is 'load'. After the 'load' state the sub-agent goes into 'active' state. In this state the sub-agent has registered with the master agent and would respond to any requests from the master agent and can also generate traps.")
sunSubAgentTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentTimeout.setDescription('The max. time for which the master agent would wait for a sub-agent to complete the request. The value is specified in usec. ')
sunSubAgentPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentPortNumber.setDescription('The port number of the sub-agent on which it listens for requests from the master agent.')
sunSubAgentRegistrationFile = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentRegistrationFile.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentRegistrationFile.setDescription('This is the registration file of a sub-agent. Each sub-agent has its own registration file. This file contains information pertinent to each agent. The information includes the name of the agent, the subtree OIDs managed by the respective agent, request time out, the preferred port number, etc.')
sunSubAgentAccessControlFile = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentAccessControlFile.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentAccessControlFile.setDescription('This is a file that has the access control information for each sub agent. It stores SNMP-related community information. Every subagent and a Master Agent can have its own access control file.')
sunSubAgentExecutable = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentExecutable.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentExecutable.setDescription('The executable file of the sub-agent.')
sunSubAgentVersionNum = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentVersionNum.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentVersionNum.setDescription('The version number of the sub-agent.')
sunSubAgentProcessID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentProcessID.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentProcessID.setDescription('The process id of the sub-agent.')
sunSubAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentName.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentName.setDescription('The name of the sub-agent. This is assigned by the user.')
sunSubAgentSystemUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 11), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentSystemUpTime.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentSystemUpTime.setDescription('The system up time of the sub-agent.')
sunSubAgentWatchDogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 8, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubAgentWatchDogTime.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubAgentWatchDogTime.setDescription('This timeout is used by the Master Agent to determine if the subagent is up or not. The Master Agent will poll the subagent only if there has been no activity between the Master Agent and the subagent for this specified interval. This interval is specified in seconds.')
sunSubTreeConfigurationTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 15, 10), )
if mibBuilder.loadTexts: sunSubTreeConfigurationTable.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeConfigurationTable.setDescription("This is the table of subtree registration requests made by the sub agents. The enteries in this table also include the sub tree OID's of those agents that are invkoed by the master agent. This table thus consists of enteries as configured in the sub agent registration files. These sub tree OID's are flattened into a OID sub tree dispatch table in the master agent which is also defined in this MIB.")
sunSubTreeConfigurationTableIndex = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 15, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSubTreeConfigurationTableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeConfigurationTableIndex.setDescription('The next available index in sunSubTreeConfigurationTable.')
sunSubTreeConfigurationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1), ).setIndexNames((0, "SUN-SEA-PROXY-MIB", "sunSubTreeAgentID"), (0, "SUN-SEA-PROXY-MIB", "sunSubTreeIndex"))
if mibBuilder.loadTexts: sunSubTreeConfigurationEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeConfigurationEntry.setDescription('An entry for table registration.')
sunSubTreeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSubTreeIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeIndex.setDescription('The index of the table registration.')
sunSubTreeAgentID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSubTreeAgentID.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeAgentID.setDescription('ID of the sub-agent.')
sunSubTreeOID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubTreeOID.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeOID.setDescription("The oid of the subtree table that is being registered. A sub agent can have multiple sub tree oid's registered as seperate enteries.")
sunSubTreeStartColumn = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubTreeStartColumn.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeStartColumn.setDescription('Starting column of the sub table.')
sunSubTreeEndColumn = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubTreeEndColumn.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeEndColumn.setDescription('Ending column of the sub table.')
sunSubTreeStartRow = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubTreeStartRow.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeStartRow.setDescription('Starting row of the sub table.')
sunSubTreeEndRow = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubTreeEndRow.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeEndRow.setDescription('Ending row of the sub table.')
sunSubTreeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubTreeStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeStatus.setDescription('The variable allows to activate or delete the enteries in this table.')
sunSubTreeDispatchTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 15, 12), )
if mibBuilder.loadTexts: sunSubTreeDispatchTable.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeDispatchTable.setDescription('This table lists all the OID enteries that are used by the master agent to dispatch the requests to the sub agents. This table is based on the sub-tree registration configured in the sub agents registration files.')
sunSubTreeDispatchTableIndex = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 15, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSubTreeDispatchTableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeDispatchTableIndex.setDescription('The next available index in sunSubTreeDispatchTable.')
sunSubTreeDispatchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 15, 12, 1), ).setIndexNames((0, "SUN-SEA-PROXY-MIB", "sunSubTreeDispatchAgentID"), (0, "SUN-SEA-PROXY-MIB", "sunSubTreeDispatchIndex"))
if mibBuilder.loadTexts: sunSubTreeDispatchEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeDispatchEntry.setDescription('An entry for tree registration.')
sunSubTreeDispatchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 12, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSubTreeDispatchIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeDispatchIndex.setDescription('The index of the dispatch table entry.')
sunSubTreeDispatchAgentID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 12, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunSubTreeDispatchAgentID.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeDispatchAgentID.setDescription('')
sunSubTreeDispatchOID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 12, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubTreeDispatchOID.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeDispatchOID.setDescription('The oid of the subtree.')
sunSubTreeDispatchStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 15, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sunSubTreeDispatchStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sunSubTreeDispatchStatus.setDescription('The variable allows to activate or delete the enteries in this table.')
mibBuilder.exportSymbols("SUN-SEA-PROXY-MIB", sunSubTreeStartColumn=sunSubTreeStartColumn, PYSNMP_MODULE_ID=sunSeaProxyMIB, sunSubAgentTable=sunSubAgentTable, sunSubAgentWatchDogTime=sunSubAgentWatchDogTime, sunSubAgentSystemUpTime=sunSubAgentSystemUpTime, sunSubAgentID=sunSubAgentID, sunSubTreeStatus=sunSubTreeStatus, sunCheckSubAgentName=sunCheckSubAgentName, sunSubTreeEndRow=sunSubTreeEndRow, sunSubTreeConfigurationEntry=sunSubTreeConfigurationEntry, sunSeaProxyMIBPollInterval=sunSeaProxyMIBPollInterval, sunSubAgentPortNumber=sunSubAgentPortNumber, sunSubTreeAgentID=sunSubTreeAgentID, sunSeaProxyMIBTrapPort=sunSeaProxyMIBTrapPort, sunSubAgentTableIndex=sunSubAgentTableIndex, sunSubTreeDispatchIndex=sunSubTreeDispatchIndex, sunSubAgentExecutable=sunSubAgentExecutable, sunSubTreeDispatchAgentID=sunSubTreeDispatchAgentID, sunSeaProxyMIB=sunSeaProxyMIB, sunSubAgentAccessControlFile=sunSubAgentAccessControlFile, sunSubTreeIndex=sunSubTreeIndex, sunSubAgentRegistrationFile=sunSubAgentRegistrationFile, sunSubTreeOID=sunSubTreeOID, sunSubTreeEndColumn=sunSubTreeEndColumn, sunSeaProxyMIBStatusFile=sunSeaProxyMIBStatusFile, sunSubAgentStatus=sunSubAgentStatus, sunSubTreeDispatchEntry=sunSubTreeDispatchEntry, sunSubTreeDispatchTableIndex=sunSubTreeDispatchTableIndex, sunSubTreeDispatchTable=sunSubTreeDispatchTable, sunSubTreeConfigurationTableIndex=sunSubTreeConfigurationTableIndex, sunSeaProxyMIBMaxAgentTimeOut=sunSeaProxyMIBMaxAgentTimeOut, sunSubAgentProcessID=sunSubAgentProcessID, sunSubAgentTimeout=sunSubAgentTimeout, sunSubAgentVersionNum=sunSubAgentVersionNum, sunSubTreeStartRow=sunSubTreeStartRow, sunSubTreeDispatchStatus=sunSubTreeDispatchStatus, sunSeaProxyMIBConfigurationDir=sunSeaProxyMIBConfigurationDir, sunSubTreeConfigurationTable=sunSubTreeConfigurationTable, sunSubAgentName=sunSubAgentName, sunSubAgentEntry=sunSubAgentEntry, sunSubTreeDispatchOID=sunSubTreeDispatchOID, sunSeaProxyMIBResourceConfigFile=sunSeaProxyMIBResourceConfigFile)
