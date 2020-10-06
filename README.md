# Election Analysis
Module 3

## Overview of Project

Providing the Board of Elections with an audit of the tabulated results of the US Congressional precinct in Colorado. This analysis will provide Tom, a Board of Elections employee, with the following information (derived from the provided election data):
<li>Total votes casted</li>
<li>The County and their specific amount of votes</li>
<li>The largest county turnout</li>
<li>Each candidate, total candidate votes, and percentage of the candidates votes</li>
<li>The winning candidate of the popular vote, candidate's winning vote count, and winning percentage</li>

### Purpose

The Board of Election is looking for a more automated audit than what is offered through Excel; which is how the audit has been conducted previously. The goal is to more efficiently provide the election audit throughout not only the Congressional districts but also the Senatorial districts and other local elections. 

## Election-Audit Results

<li>369, 711 total votes were casted for the US Congressional election</li>
<li>The breakdown of the counties participating in the US Congressional election are:</li>
<p class="tab">1. Denver - 82.8% with 306,055 votes</p>
<p class="tab">2. Jefferson - 10.5% with 38,855 votes</p>
<p class="tab">3. Arapahoe - 6.7% with 24, 801 votes</p>
<li>The county with the largest voting turnout is Denver</li>
<li>The breakdown of the candidate results in the US Congressional election are:</li>
	1. Diana DeGette - 73.8% with 272,892 votes
	2. Charles Casper Stockham - 23% with 85,213 votes
	3. Raymon Anthony Doane - 3.1% with 11,606 votes
<li>The winning candidate, determined by popular vote, is:</li>
	*Diana DeGette - 73.8% with 272,892 votes</li>

<img src="Resources/election_audit_results" alt="Election Audit Results">

## Election-Audit Summary

The possibilities and efficiencies are a driving factor to utilizing Python over Excel for a more automated, easily edited, and organized format to provide election result based audit. The written code creates dictionaries and lists to house the the independent variables which are replaceable by re-defining the variables to suit the audit needed. The  variable assignments utilized in this program can be used to for different cities, counties, and states based on the provided election results as well as the candidate variable be representating candidates or amendments up for election by providing alternative election results and re-defining the variables. When looking at the code for collecting an item or name and then counting the votes for that particular input - your possibilities are endless of what information can be collected and tallied electronically.
 
